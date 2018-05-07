import changeLocation from './changeLocation';
import getPetDetails from './getPetDetails';
import newUser from './newUser';
import searchPets from './searchPets';
import submitPet from './submitPet';
import submitShelter from './submitShelter';
import updatePassword from './updatePassword';
import updatePet from './updatePet';
import updateShelter from './updateShelter';
import updateUsername from './updateUsername';
import userLogin from './userLogin';
import setSearchCriteria from './setSearchCriteria';
import showSearchResults from './showSearchResults';
import getUserDetails from './getUserDetails';

export const types = {
    CHANGE_LOCATION: 'CHANGE_LOCATION',
    GET_PET_DETAILS: 'GET_PET_DETAILS',
    SUBMIT_USER: 'CREATE_USER',
    SEARCH_PETS: 'SEARCH_PETS',
    SUBMIT_PET: 'SUBMIT_PET',
    SUBMIT_SHELTER: 'SUBMIT_SHELTER',
    UPDATE_PASSWORD: 'UPDATE_PASSWORD',
    UPDATE_PET: 'UPDATE_PET',
    UPDATE_SHELTER: 'UPDATE_SHELTER',
    UPDATE_USERNAME: 'UPDATE_USERNAME',
    LOGIN_USER: 'LOGIN_USER',
    SET_SEARCH: 'SET_SEARCH',
    SHOW_SEARCH: 'SHOW_SEARCH',
    GET_USER_DETAILS: 'GET_USER_DETAILS'
};

export {
    changeLocation,
    getPetDetails,
    newUser,
    searchPets,
    submitPet,
    submitShelter,
    updatePassword,
    updatePet,
    updateShelter,
    updateUsername,
    userLogin,
    setSearchCriteria,
    showSearchResults,
    getUserDetails
};

