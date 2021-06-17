export const initialState = {
  customers: [],
};

export const reducer = (state, action) => {
  switch (action.type) {
    case "GET_CUSTOMERS":
      return {
        ...state,
        customers: action.customers,
      };
    default:
      return state;
  }
};
