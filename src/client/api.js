/* global PRODUCTION */

import fetch from 'isomorphic-fetch';

const host = (PRODUCTION) ? '' : 'http://localhost:5000';


export function helloWorld(){
    return fetch(`${host}/v1/hello`)
    .then(response => {
        if (response.ok) return response.json();
        else return Promise.reject(new Error('Could not connect to hello world'))
    })

}

/*

formData = {"username":usr, "password":pss}
*/

export function userLogin(formData) {
  return fetch(host + '/v1/user/', {
    method: 'POST',
    body: formData
  }).then(response => {
    if (response.ok) return response.json();
    else return response.json().then(json => {
      return Promise.reject(new Error(json.error_message));
    });
  });
}

export function getUserDetails(user_id) {
  return fetch(`${host}/v1/users/user_id`)
    .then(response => {
      if (response.ok) return response.json();
      else return Promise.reject(new Error('Could not fetch user details'));
    });
}

export function getPetDetials(pet_id) {
    return fetch(`${host}/v1/pets/pet_id`)
        .then(response => {
            if(response.ok) return response.json();
            else return Promise.rejection(new Error('Could not fetch pet details'));
        });
}

/*

formData = {"age_min": int
            "age_max": int
            "weight_min": int
            "weight_max": int
            "user_city" string
            "breed": string
            "species": string

*/

export function searchPets(formData) {
  return fetch(host + '/v1/pets/', {
    method: 'POST',
    body: formData
  }).then(response => {
    if (response.ok) return response.json();
    else return response.json().then(json => {
      return Promise.reject(new Error(json.error_message));
    });
  });
}


export function searchShelters(shelter_search_input) {

  return fetch(`${host}/shelters/`, {
    method: 'POST',
    body: shelter_search_input
  })
    .then(response => {
      if (response.ok) return response.json();
      else return response.json().then(json => {
        return Promise.reject(new Error(json.error_message))
      });
    });
}