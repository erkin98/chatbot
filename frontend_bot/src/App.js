import './App.css';
import {useEffect} from 'react';
import axios from 'axios';
import  {BrowserRouter as Router,Route,Switch} from 'react-router-dom';
import Chat from "./Chat";
import Login from "./Login";
import Sidebar from "./Sidebar";
import { useStateValue } from './StateProvider';


function App() {
  const [state, dispatch] = useStateValue();
  const fetchData = async() => {
    try{
      const res = await axios.get('/customers');
      // console.log(res.data);
      dispatch({ type: "GET_CUSTOMERS", customers: res.data.data });
      return res;
    }catch(err){ console.log(err) }
  };
  useEffect(() => {
    let intervalId;
      fetchData();
      intervalId = setInterval(fetchData,30000);
    return () => clearInterval(intervalId); //cleanup function
  }, []);

  return (
    <div className="app">
      <div className="app__body">
          <Router>
            <Sidebar />
            <Switch>
              <Route path="/rooms/:roomId">
                <Chat />
              </Route>
              <Route path="/"></Route>
            </Switch>
          </Router>
        </div>
    </div>
  );
}

export default App;
