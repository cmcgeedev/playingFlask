import { combineReducers } from 'redux';
import { petsReducer, petReducer } from './petReducers';
import { sheltersReducer, shelterReducer } from './shelterReducers';
import login from './login';
import petsReducer from './petsReducer';
import petSearch from './petSearch';
import shelter from './shelter';
import ui from './ui';
import user from './user';


export default combineReducers({
  login,
  pet,
  petSearch,
  shelter,
  ui,
  user
});