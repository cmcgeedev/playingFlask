import { types } from '../actions/'

const defaultState = {
    logged_in: null,
    selectedPet: {
        pet_id: null,
        pet_name: null,
        pet_age: null,
        pet_weight: null,
        pet_height: null
    },
    sort: {
        field: 'created_date',
        isAsc: false
    },
    paging: {
        page: 0,
        totalPages: null
    },
    search_criteria: {
        species: null,
        breed: null,
        age_min: null,
        age_max: null,
        weight_min: null,
        weight_max: null
    },
    pet_list: []
}