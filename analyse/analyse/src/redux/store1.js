import { configureStore } from '@reduxjs/toolkit';


const initialState = {

  FileSelected: "",
  ListFiles:"",
  DataJson:"",
  inputIP:"all",
  selectedProtocol:"all",
  checkPing:false,
  selectedDate:'',
  display:'list',
  hoteObj:'',
  httpopen:[],
  sshopen:[],
  sqlopen:[],
  ftpopen:[],
};

export const filtreIP = (ip) => ({
  type: "filtreIP",
  ip:ip
})

export const filtreProtocol = (protocol) => ({
  type: "filtreProtocol",
  protocol:protocol
})

export const filtrePing = (ping) => ({
  type: "filtrePing",
  ping:ping
})

export const filtreDate = (date) => ({
  type: "filtreDate",
  date:date
})

export const changeFile = (data,file) => ({
    file: file,
    type: "FILE_DATA_RECEIVED",
    payload: data
});

export const filtreDisplay = (display) => ({
  type: "filtreDisplay",
  display:display
})

export const displayHote = (hote) => ({
  type: "displayHote",
  hote:hote
})



function reducer(state, action) {
  let newState;
  switch (action.type) {
    case "FILE_DATA_RECEIVED":
      newState =  {
        ...state,
        FileSelected: action.file,
        DataJson: action.payload.contenu
      };
      break;

    case "filtreIP":
        newState =  {
          ...state,
          inputIP: action.ip
        };
        break;

    case "filtreProtocol":
        newState =  {
          ...state,
          selectedProtocol: action.protocol
        };
        break;
    case "filtrePing":
        newState =  {
          ...state,
          checkPing: action.ping
        };
        break;
    case "filtreDate":
        newState =  {
          ...state,
          selectedDate: action.date
        };
        break;
    case "filtreDisplay":
        newState =  {
          ...state,
          display: action.display
        };
        break;
    case "displayHote":
      newState =  {
        ...state,
        hoteObj: action.hote
      };
        break;
        
        
    default:
      newState = state;
      break;
  }

  return newState;
}

const store1 = configureStore({
  reducer: reducer,
  preloadedState: initialState,
});




export default store1;
