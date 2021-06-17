import { Avatar, IconButton } from "@material-ui/core";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import { SearchOutlined } from "@material-ui/icons";
import InsertEmoticonIcon from "@material-ui/icons/InsertEmoticon";
import AttachFileIcon from "@material-ui/icons/AttachFile";
import MicIcon from "@material-ui/icons/Mic";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./Chat.css";
import axios from 'axios';
import { useStateValue } from "./StateProvider";
function Chat() {
  const [seed, setSeed] = useState("");
  const [message, setMessage] = useState("");
  const { roomId } = useParams();
  const [messages, setMessages] = useState([]);
  const [state, dispatch] = useStateValue();
  const fetchData = async() => {
    try{
      const res = await axios.get('/'+state.customers[roomId]);
      setMessages(res?.data?.data.reverse());
      return res;
    }catch(err){ console.log(err); return err; }
  };
  useEffect(() => {
    let intervalId;
    if (roomId) {
      setMessages([]);
      fetchData();
      intervalId = setInterval(fetchData,32000);
    }
    return () => clearInterval(intervalId); //cleanup function
  }, [roomId]);
  
  return (
    <div className="chat">
      <div className="chat__header">
        <div className="chat__header__left">
          <Avatar src={`https://avatars.dicebear.com/api/human/${seed}.svg`} />
          <div className="chat__header__info">
            <h3>{state.customers[roomId]}</h3>
          </div>
        </div>
        <div className="chat__header__right">
          <IconButton>
            <SearchOutlined />
          </IconButton>
          <IconButton>
            <MoreVertIcon />
          </IconButton>
        </div>
      </div>
      <div className="chat__body">
        {messages?.map((mes) => {
          return mes?.map((s,idx)=>
              <p
              key={`msg-${idx}`}
            className={`chat__message ${
              mes?.indexOf(s) == 1 && "chat__reciever"
            }`}
          >
            {s}
          </p>
        )
        })}
      </div>
      <div className="chat__footer">
        <IconButton>
          <InsertEmoticonIcon />
        </IconButton>
        <IconButton>
          <AttachFileIcon />
        </IconButton>
        <form>
          <input
            type="text"
            value={message}
            placeholder="Type a message"
            onChange={(e) => setMessage(e.target.value)}
          />
          <button type="submit" onClick={()=>{}}>
            Send a message
          </button>
        </form>

        <IconButton>
          <MicIcon />
        </IconButton>
      </div>
    </div>
  );
}

export default Chat;
