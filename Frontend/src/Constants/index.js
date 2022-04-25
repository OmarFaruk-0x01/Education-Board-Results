import {PermissionsAndroid, Platform} from 'react-native';
import {HomeScreen, ResultScreen} from '../Screens/';
import RNSF from 'react-native-fs';

export const BASEURL = 'http://127.0.0.1:5000';

export const DownloadDir = Platform.OS === 'android' ?
  RNSF.ExternalStorageDirectoryPath + '/Documents/EDU_RESULT' : RNSF.DocumentDirectoryPath + '/EDU_RESULT';
export const ROUTE = [
  {
    name: 'Home',
    key: 'home-page',
    Component: HomeScreen,
  },
  {
    name: 'Result_Details',
    key: 'result-details-page',
    Component: ResultScreen,
  },
];

export const EXAM = [
  ['JSC/JDC', 'JSC/JDC'],
  ['SSC(Vocational)', 'SSC(Vocational)'],
  ['SSC/Dakhil', 'SSC/Dakhil'],
  ['HSC/Alim/Equivalent', 'HSC/Alim/Equivalent'],
  ['HSC(Vocational)', 'HSC(Vocational)'],
  ['HSC(BM)', 'HSC(BM)'],
  ['Diploma in Commerce', 'Diploma in Commerce'],
  ['Diploma in Business Studies', 'Diploma in Business Studies'],
];

export const BOARD = [
  ['Dhaka', 'Dhaka'],
  ['Barisal', 'Barisal'],
  ['Chittagong', 'Chittagong'],
  ['Comilla', 'Comilla'],
  ['Dinajpur', 'Dinajpur'],
  ['Jessore', 'Jessore'],
  ['Mymensingh', 'Mymensingh'],
  ['Rajshahi', 'Rajshahi'],
  ['Shylet', 'Shylet'],
  ['Madrasah', 'Madrasah'],
  ['Technical', 'Technical'],
  ['DIBS(Dhaka)', 'DIBS(Dhaka)'],
];

const currentYear = new Date(new Date().getTime()).getUTCFullYear();

export const YEAR = Array(40)
  .fill(null)
  .map((i, index) => [currentYear - (index + 1), currentYear - (index + 1)]);

export let requestStoragePermission = async () => {
  try {
    if (Platform.OS === 'android') {
      const granted = await PermissionsAndroid.request(
        PermissionsAndroid.PERMISSIONS.WRITE_EXTERNAL_STORAGE,
      );
  
      return granted === PermissionsAndroid.RESULTS.GRANTED;
    } else {
      return true;
    }
  } catch (err) {
    console.warn(err);
  }
};
