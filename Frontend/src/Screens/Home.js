import React, {useState} from 'react';
import {TextInput, Button, Banner, Snackbar} from 'react-native-paper';
import {View, Image} from 'react-native';
import {AppHeader, DropDownMenu} from '../Components';
import {BASEURL, BOARD, EXAM, YEAR} from '../Constants';
import RNSF from 'react-native-fs';

const HomeScreen = function ({navigation}) {
  const [bannerVisible, setBannerVisible] = useState(false);
  const [load, setLoad] = useState(false);
  const [exam, setExam] = useState(null);
  const [board, setBoard] = useState(null);
  const [year, setYear] = useState(null);
  const [boardRoll, setBoardRoll] = useState('');
  const [boardReg, setBoardReg] = useState('');
  const [snackVisiable, setSnackVisiable] = useState(false);
  const [snackMessage, setSnackMessage] = useState('');

  const ResetAllInput = React.useCallback(function () {
    setExam(null);
    setYear(null);
    setBoard(null);
    setBoardRoll('');
    setBoardReg('');
  }, []);
  function navigateToResult() {
    setLoad(true);
    if (
      exam == null ||
      board == null ||
      year == null ||
      boardRoll == '' ||
      boardReg == ''
    ) {
      ToggleSnackbar('Please Enter All Info');
      setLoad(false);
      return;
    }
    fetch(BASEURL + '/getresult', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        board,
        year,
        exam,
        roll: boardRoll,
        reg: boardReg,
      }),
    })
      .then(data => {
        return data.json();
      })
      .then(data => {
        setLoad(false);
        if (data.StatusCode !== 200) {
          ToggleSnackbar(data.message);
        } else {
          ResetAllInput();
          navigation.navigate('Result_Details', {data: {exam, ...data}});
        }
      })
      .catch(e => {
        setLoad(false);
        ToggleSnackbar(data.message);
      });
  }
  function CheckServer() {
    RNSF.exists(
      RNSF.ExternalStorageDirectoryPath + '/Documents/EDU_RESULT',
    ).then(b => {
      if (!b) {
        RNSF.mkdir(RNSF.ExternalStorageDirectoryPath + '/Documents/EDU_RESULT');
      }
    });
    fetch(BASEURL + '/')
      .then(data => data.json())
      .then(data => {
        if (data.message !== 'ok') {
          setBannerVisible(true);
        }
      });
  }

  const ToggleSnackbar = React.useCallback(function (msg) {
    setSnackMessage(msg);
    setSnackVisiable(true);
  }, []);

  function SnackOnDismiss() {
    setSnackVisiable(false);
  }

  React.useEffect(() => {
    CheckServer();
  }, []);

  return (
    <>
      <AppHeader />
      <Snackbar
        duration={1000}
        style={{backgroundColor: '#fe3025'}}
        color={'#fff'}
        onDismiss={SnackOnDismiss}
        visible={snackVisiable}>
        {snackMessage}
      </Snackbar>
      <Banner
        contentStyle={{color: 'red', backgroundColor: '#f000000f'}}
        visible={bannerVisible}
        actions={[
          {
            label: 'Retry',

            onPress: () => {
              setBannerVisible(false);
              CheckServer();
            },
          },
        ]}
        icon={({size}) => (
          <Image
            source={{
              uri: 'https://cdn-icons-png.flaticon.com/512/463/463612.png',
            }}
            style={{
              width: size,
              height: size,
            }}
          />
        )}>
        Education Board Result Server Currently Down. Please Try again after
        sometime.
      </Banner>

      <View style={{flex: 1, backgroundColor: '#fff', paddingHorizontal: 5}}>
        <DropDownMenu
          title={'Choose Examination'}
          menuList={EXAM}
          onChangeHandler={setExam}
          value={exam}
        />
        <DropDownMenu
          title={'Choose Board'}
          menuList={BOARD}
          onChangeHandler={setBoard}
          value={board}
        />
        <DropDownMenu
          title={'Choose Year'}
          menuList={YEAR}
          onChangeHandler={setYear}
          value={year}
        />
        <TextInput
          style={{
            marginVertical: 10,
            backgroundColor: '#efefef',
            marginHorizontal: 0,
            color: '#000',
          }}
          placeholderTextColor={'#000'}
          label="Board Roll"
          value={boardRoll}
          keyboardType="numeric"
          maxLength={10}
          onChangeText={text => setBoardRoll(text)}
        />
        <TextInput
          label="Board Regestretion"
          style={{backgroundColor: '#efefef', color: '#000'}}
          value={boardReg}
          keyboardType="numeric"
          placeholderTextColor={'#000'}
          maxLength={15}
          onChangeText={text => setBoardReg(text)}
        />
        <View style={{flex: 1}}></View>
        <Button
          onPress={navigateToResult}
          style={{marginBottom: 10}}
          mode={'contained'}
          labelStyle={{color: '#fff'}}
          loading={load}>
          Submit
        </Button>
      </View>
    </>
  );
};

export default HomeScreen;
