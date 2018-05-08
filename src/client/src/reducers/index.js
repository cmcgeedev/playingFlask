import { combineReducers } from 'redux';
import { petsReducer, petReducer } from './petReducers';
import { sheltersReducer, shelterReducer } from './shelterReducers';
import login from './login';
import { LoginUiReducer } from './LoginUiReducers';
import { userReducer } from './userReducers';


export default combineReducers({
  petsReducer,
  petReducer,
  LoginUiReducer,
  sheltersReducer,
  shelterReducer,
  userReducer
});