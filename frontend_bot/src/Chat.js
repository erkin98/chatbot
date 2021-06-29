import React, { useCallback, useEffect, useRef, useState } from "react";
import PersonIcon from '@material-ui/icons/Person';
import { Avatar, makeStyles } from "@material-ui/core";
import { useParams } from "react-router-dom";
import "./Chat.css";
import axios from 'axios';
import { useStateValue } from "./StateProvider";

const useStyles = makeStyles((theme) => ({
  large: {
    width: "50px",
    height: "50px",
  },
}));

function Chat() {
  const { roomId } = useParams();
  const [messages, setMessages] = useState([]);
  const [state] = useStateValue();
  const classes = useStyles();
  const divRef = useRef(null);
  const fetchData = useCallback(async() => {
    try{
      setMessages([]);
      const res = await axios.get('/'+state.customers[roomId]);
      setMessages(res?.data?.data.reverse());
      return res;
    }catch(err){ console.log(err); return err; }
  },[roomId,state.customers]) 
  useEffect(() => {
      setMessages([]);
      fetchData();
  }, [roomId,fetchData]);
  
  useEffect(() => {
    const reference = divRef.current;
    const nodeInserted = event => {
      const { currentTarget } = event;
      currentTarget.scroll({ top: currentTarget.scrollHeight, behavior: 'smooth' });
    }
    if (divRef) {
      reference.addEventListener('DOMNodeInserted', nodeInserted);
    }
    return ()=> reference.removeEventListener("DOMNodeInserted",nodeInserted);
  }, []);

  return (
    <div className="chat">
      <div className="chat__header">
        <div className="chat__header__left">
          <div className="chat__header__info">
              <Avatar
              src={<PersonIcon/>}
              className={classes.large}
            />
            <h3>{state.customers[roomId]}</h3>
          </div>
        </div>
      </div>
      <div className="chat__body" ref={divRef}>
        {messages?.map((mes) => {
          return mes?.map((s,idx)=>
              <p
              key={`msg-${idx}`}
            className={`chat__message ${
              mes?.indexOf(s) === 1 && "chat__reciever"
            }`}
          >
            {s}
          </p>
        )
        })}
      </div>
    </div>
  );
}

export default Chat;
