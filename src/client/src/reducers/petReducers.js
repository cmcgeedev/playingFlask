export const petsReducer(state = [], action) {
  switch (action.type) {
    case SEARCH_PETS:
        if (action.meta.status === 'success') return action.pets
    default:
      return state
  }
}

export const petReducer = (state=[], action) => {

    switch(action.type) {
        case UPDATE_PET:
            if (action.meta.status === 'success') return Object.assign({}, state, {pet: action.payload})
        case SUBMIT_PET:
            if (action.meta.status === 'success') return Object.assign({}, state, {pet: action.payload})
        case GET_PET_DETAILS:
            if (action.meta.status === 'success') return Object.assign({}, state, {pet: action.payload})
        default:
            return state
    }
}