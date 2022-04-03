import React, {useState} from 'react';
import {Button, Dialog, Portal, RadioButton, Text} from 'react-native-paper';
import {View, FlatList, ScrollView} from 'react-native';

const DialogPortal = React.memo(function ({
  visible,
  hideDialog,
  value,
  setValue,
  menuList,
}) {
  const setRadioValue = React.useCallback(value => {
    hideDialog();
    setValue(value);
  }, []);
  return (
    <Portal>
      <Dialog visible={visible} onDismiss={hideDialog}>
        <Dialog.ScrollArea style={{padding: 0}}>
          <ScrollView showsVerticalScrollIndicator={false}>
            <RadioButton.Group
              mode="ios"
              onValueChange={value => setRadioValue(value)}
              value={value}>
              <RadioButton.Item label="Choose Examination" disabled />
              {menuList.map(item => (
                <RadioButton.Item
                  key={item[0]}
                  label={item[0]}
                  value={item[1]}
                />
              ))}
            </RadioButton.Group>
          </ScrollView>
        </Dialog.ScrollArea>
      </Dialog>
    </Portal>
  );
});

const DropDownMenu = function ({menuList, title, onChangeHandler, value}) {
  const [visible, setVisible] = useState(false);

  function hideDialog() {
    setVisible(false);
  }

  const buttonText = value !== null ? value : title;
  return (
    <View
      style={{
        flexDirection: 'row',
        alignItems: 'center',
        marginVertical: 5,
        justifyContent: 'space-between',
      }}>
      <Text style={{fontSize: 18, color: '#5f5f5f'}}>{title}</Text>
      <Button
        style={{
          width: 170,
          paddingHorizontal: 4,
          fontSize: 20,
          marginTop: 5,
          backgroundColor: value !== null ? '#8e11c4' : '#efefef',
        }}
        icon={{
          source: 'arrow-bottom-right-thick',
          direction: 'ltr',
          fontSize: 15,
        }}
        labelStyle={{
          fontSize: 20,
          color: value !== null ? '#fff' : '#000',
          direction: 'ltr',
        }}
        mode="contained"
        onPress={() => {
          setVisible(true);
        }}
        color="#efefef">
        <Text
          style={{
            fontSize: 15,
            width: '100%',
            color: value !== null ? '#ffff' : '#000',
          }}>
          {buttonText}
        </Text>
      </Button>

      <DialogPortal
        value={value}
        hideDialog={hideDialog}
        visible={visible}
        setValue={onChangeHandler}
        menuList={menuList}
      />
    </View>
  );
};

export default DropDownMenu;
