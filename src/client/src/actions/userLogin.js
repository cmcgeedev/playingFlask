import { types } from './index';
import * as api from '../api';

function userLoginRequest() {
  return { type: types.LOGIN_USER, meta: { status: 'request' } };
}

function userLoginSuccess(json) {
  return {
    type: types.LOGIN_USER,
    meta: { status: 'success' },
    payload: json.message
  };
}

function userLoginFail(error) {
  return {
    type: types.LOGIN_USER,
    meta: { status: 'error' },
    error: true,
    payload: { message: error }
  };
}

export default function userLogin(formData) {
  return (dispatch) => {
    dispatch(userLoginRequest(formData));

    return api.userLogin(formData)
      .then(json => dispatch(userLoginSuccess(json)))
      .catch(error => dispatch(userLoginFail(error.message)));
  };
}
