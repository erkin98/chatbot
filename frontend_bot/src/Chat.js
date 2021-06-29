import { IconButton } from '@material-ui/core';
import RefreshIcon from '@material-ui/icons/Refresh';

import React, { useCallback, useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import "./Chat.css";
import axios from 'axios';
import { useStateValue } from "./StateProvider";
function Chat() {
  const { roomId } = useParams();
  const [messages, setMessages] = useState([]);
  const [state] = useStateValue();
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
    if (divRef) {
      divRef.current.addEventListener('DOMNodeInserted', event => {
        const { currentTarget } = event;
        currentTarget.scroll({ top: currentTarget.scrollHeight, behavior: 'smooth' });
      });
    }
  }, []);

  return (
    <div className="chat">
      <div className="chat__header">
        <div className="chat__header__left">
          <div className="chat__header__info">
            <h3>{state.customers[roomId]}</h3>
          </div>
        </div>
        <div className="chat__header__right">
          <IconButton onClick={fetchData}>
            <RefreshIcon/>
          </IconButton>
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
