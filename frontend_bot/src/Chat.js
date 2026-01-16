import React, { useCallback, useEffect, useRef, useState } from "react";
import PersonIcon from '@material-ui/icons/Person';
import { Avatar, makeStyles } from "@material-ui/core";
import { useParams } from "react-router-dom";
import "./Chat.css";
import axios from 'axios';
import { useStateValue } from "./StateProvider";
import Spinner from './Spinner';

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
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);
  const sizeRef = useRef(10);
  
  const classes = useStyles();
  const chatBodyRef = useRef(null);
  const prevScrollHeight = useRef(0);
  const isLoadMore = useRef(false);

  const fetchMessages = useCallback(async () => {
    if (!state.customers || !state.customers[roomId]) return;
    
    setLoading(true);
    try {
      const currentSize = sizeRef.current;
      // Using axios.post as per original implementation
      const res = await axios.post(`/customers/${state.customers[roomId]}`, { size: currentSize });
      
      const allMessages = res.data.data || [];
      // Original logic reversed the list because backend sends [latest...oldest] (implied by client.messages.list default order usually being desc date, but we zip them. 
      // If backend logic didn't change order, we assume it's consistent.
      // Original: setMessages(res?.data?.data?.reverse()) for initial load.
      
      const reversedMessages = [...allMessages].reverse();
      setMessages(reversedMessages);

      // Heuristic for "has more": if we got fewer messages (tuples) than we asked for (limit), we probably exhausted the history.
      // Note: Twilio list returns up to limit.
      if (allMessages.length < currentSize) {
         // This logic is imperfect because if we have exactly 10 messages and ask for 10, we get 10. Next time we ask for 20, we get 10.
         // But we can't easily detect "end" without a count or next_page_uri from backend.
         // We'll leave it as is.
      }
      
    } catch (err) {
      console.error("Error fetching messages:", err);
    } finally {
      setLoading(false);
    }
  }, [roomId, state.customers]);

  useEffect(() => {
    // Initial Load
    setMessages([]);
    sizeRef.current = 10;
    setHasMore(true);
    isLoadMore.current = false;
    fetchMessages();
  }, [roomId, fetchMessages]);

  useEffect(() => {
    // Handle Scroll Position
    const chatBody = chatBodyRef.current;
    if (chatBody) {
      if (isLoadMore.current) {
        // Restore scroll position relative to bottom
        chatBody.scrollTop = chatBody.scrollHeight - prevScrollHeight.current;
        isLoadMore.current = false;
      } else {
        // Scroll to bottom on initial load
        chatBody.scrollTop = chatBody.scrollHeight;
      }
    }
  }, [messages]);

  const handleLoadMore = () => {
    if (chatBodyRef.current) {
      prevScrollHeight.current = chatBodyRef.current.scrollHeight;
    }
    isLoadMore.current = true;
    sizeRef.current += 10;
    fetchMessages();
  };

  return (
    <div className="chat">
      <div className="chat__header">
        <div className="chat__header__left">
          <div className="chat__header__info">
            <Avatar src={<PersonIcon/>} className={classes.large} />
            <h3>{state.customers ? state.customers[roomId] : 'User'}</h3>
          </div>
        </div>
      </div>
      
      <div className="chat__body" ref={chatBodyRef}>
        <div className="chat__size" style={{ display: hasMore ? 'block' : 'none' }}> 
            <div className="chat__size__inner">
              {loading ? <Spinner/> : <div className="chat__size__icon" onClick={handleLoadMore}>+10</div>}
            </div>
        </div>
        
        {messages.map((mes, groupIdx) => (
             mes.map((msgContent, msgIdx) => (
                <div key={`${groupIdx}-${msgIdx}`} className="messages">
                     <p className={`chat__message ${msgIdx === 1 ? "chat__reciever" : ""}`}>
                        {msgContent}
                     </p>
                </div>
             ))
        ))}
      </div>
    </div>
  );
}

export default Chat;
