import { types } from './index';
import * as api from '../api';

function getPetDetailsRequest() {
    return { type: types.GET_PET_DETAILS, meta: { status: 'request'}};
}

function getPetDetailsSuccess(json) {
    console.log('successfully oobtained pet info');
    console.log(json);
    return {
        type: types.GET_PET_DETAILS,
        meta: {status: 'success' },
        payload: json
    };
}

function getPetDetailsFail(error) {
  return {
    type: types.GET_PET_DETAILS,
    meta: { status: 'error' },
    error: true,
    payload: { message: error }
  };
}

export default function getPetDetails(petId){
    return (dispatch, getState) => {
    const { pet } = getState();
    dispatch(getPetDetailsRequest());

    return api.getPetDetails(pet.id)
        .then(json => dispatch(getPetDetailsSuccess(json)))
        .catch(error => dispatch(getUserFail(error.message)));
    }
}