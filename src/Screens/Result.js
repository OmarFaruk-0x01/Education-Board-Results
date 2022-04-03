import {useRoute, useNavigation} from '@react-navigation/native';
import React from 'react';
import {
  ScrollView,
  View,
  ToastAndroid,
  NativeModules,
  Alert,
} from 'react-native';
import {
  Button,
  DataTable,
  Dialog,
  Portal,
  ProgressBar,
  Text,
} from 'react-native-paper';
import {AppHeader} from '../Components';
import {BASEURL, DownloadDir, requestStoragePermission} from '../Constants';
import RNSF from 'react-native-fs';
const SingleInfoView = function ({Key, Value, title}) {
  if (title) {
    return (
      <View
        style={{
          flexDirection: 'row',
          alignItems: 'center',
          justifyContent: 'center',
          padding: 10,
          marginTop: 10,
          marginHorizontal: 10,
          backgroundColor: '#efefef',
          borderRadius: 7,
        }}>
        <Text
          style={{
            flex: 1,
            textAlign: 'center',
            color: '#afafaf',
          }}>
          {title}
        </Text>
      </View>
    );
  }
  return (
    <View
      style={{
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: 10,
        marginTop: 10,
        marginHorizontal: 10,
        backgroundColor: '#efefef',
        borderRadius: 7,
      }}>
      <Text
        style={{
          borderRightWidth: 1,
          borderRightColor: '#cfcfcf',
          flex: 1,
          textAlign: 'left',
          color: '#6f6f6f',
        }}>
        {Key}
      </Text>
      <Text
        style={{
          borderLeftWidth: 1,
          borderLeftColor: '#cfcfcf',
          flex: 1,
          textAlign: 'right',
          color:
            Key == 'Result' && Value !== 'PASSED'
              ? 'red'
              : Key == 'Result' && Value == 'PASSED'
              ? 'green'
              : Key == 'GPA' && parseFloat(Value) > 4.0
              ? 'green'
              : 'black',
        }}>
        {Value}
      </Text>
    </View>
  );
};

const DownloadButton = function ({data: MainData}) {
  const [visible, setVisiable] = React.useState(false);
  const [load, setLoad] = React.useState(false);
  const [progress, setProgress] = React.useState(0);
  function hideDialog() {
    setVisiable(false);
  }

  function downLoad() {
    setLoad(true);
    fetch(BASEURL + '/genPDF', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(MainData),
    })
      .then(data => {
        // // console.log(data.status);
        if (data.status !== 200) {
          setLoad(false);
          Alert.alert(
            'Error',
            'Internal Server Error. Contact with developer.',
          );
          return;
        }
        return data.json();
      })
      .then(data => {
        if (!data) {
          return;
        }
        ToastAndroid.showWithGravity(
          data.message,
          ToastAndroid.SHORT,
          ToastAndroid.BOTTOM,
        );
        setLoad(false);
        setVisiable(true);
        // // console.log(data);
        // fetch(data.downLink)
        //   .then(data => {
        //     return data.formData();
        //   })
        //   .then(data => {
        // console.log(data);
        //   });
        requestStoragePermission().then(isGranted => {
          if (isGranted) {
            RNSF.downloadFile({
              fromUrl: data.downLink,
              toFile: `${DownloadDir}/${MainData.roll}_${MainData.exam.replace(
                '/',
                '-',
              )}_Result.pdf`,

              progress: data => {
                const percentage =
                  ((100 * data.bytesWritten) / data.contentLength) | 0;
                setProgress(percentage);
              },
            })
              .promise.then(data => {
                setVisiable(false);
                if (data.statusCode !== 200) {
                  Alert.alert('Failed!', 'Downloading Failed. Try again');
                } else {
                  ToastAndroid.showWithGravity(
                    'Download Complete',
                    ToastAndroid.SHORT,
                    ToastAndroid.BOTTOM,
                  );
                }
              })
              .catch(e => {
                setVisiable(false);
                Alert.alert('Failed!', e.toString());
                // console.log(e);
              });
          }
          // PdfHandler.downloadFile(
          //   data.downLink,
          //   `${MainData.roll}_Result.pdf`,
          //   file => {
          //     // console.log(file);
          //   },
          // );
        });
      });
  }

  return (
    <>
      <Button
        onPress={downLoad}
        icon={'download'}
        mode={'contained'}
        loading={load}
        labelStyle={{color: '#fff'}}
        style={{margin: 5}}>
        {load == true ? 'Generating PDF' : 'Download PDF'}
      </Button>
      <Portal>
        <Dialog visible={visible} onDismiss={hideDialog}>
          <Dialog.Title> Downloading...</Dialog.Title>
          <Dialog.Content>
            <ProgressBar progress={progress} />
          </Dialog.Content>
        </Dialog>
      </Portal>
    </>
  );
};

const ResultScreen = function () {
  const nav = useNavigation();
  const {
    params: {data},
  } = useRoute();
  return (
    <>
      <AppHeader withBackButton={true} />

      <ScrollView style={{flex: 1, backgroundColor: '#fff'}}>
        <SingleInfoView Key={'Roll NO.'} Value={data.roll} />
        <SingleInfoView Key={'Name'} Value={data.name} />
        <SingleInfoView Key={"Father's Name"} Value={data.father_name} />
        <SingleInfoView Key={"Mother's Name"} Value={data.mother_name} />
        <SingleInfoView Key={'Date Of Birth'} Value={data.dob} />
        <SingleInfoView Key={'Institute'} Value={data.institute} />
        <SingleInfoView Key={'Board'} Value={data.board} />
        <SingleInfoView Key={'Group'} Value={data.group} />
        <SingleInfoView Key={'Type'} Value={data.type} />
        <SingleInfoView Key={'Result'} Value={data.result} />
        <SingleInfoView Key={'GPA'} Value={data.gpa} />
        <SingleInfoView Key={''} title={'Grade Sheet'} Value={''} />
        <DataTable>
          <DataTable.Header>
            <DataTable.Title>Subject</DataTable.Title>
            <DataTable.Title numeric>Subject Code</DataTable.Title>
            <DataTable.Title numeric>Grade</DataTable.Title>
          </DataTable.Header>

          {data.subject_grades.map(item => (
            <DataTable.Row key={item.subjectCode}>
              <DataTable.Cell>{item.subjectName}</DataTable.Cell>
              <DataTable.Cell numeric>{item.subjectCode}</DataTable.Cell>
              <DataTable.Cell numeric>{item.subjectGPA}</DataTable.Cell>
            </DataTable.Row>
          ))}
        </DataTable>
      </ScrollView>
      <DownloadButton data={data} />
    </>
  );
};

export default ResultScreen;
