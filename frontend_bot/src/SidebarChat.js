import React, { useEffect, useState } from "react";
import "./SidebarChat.css";
import { Avatar, makeStyles } from "@material-ui/core";
import { Link } from "react-router-dom";
const useStyles = makeStyles((theme) => ({
  large: {
    width: "50px",
    height: "50px",
  },
}));

function SidebarChat({ id, addNewChat, name }) {
  const classes = useStyles();
  const [seed, setSeed] = useState("");
  // const [messages, setMessages] = useState([]);

  // useEffect(() => {
  //   if (id) {
  //     db.collection("rooms")
  //       .doc(id)
  //       .collection("messages")
  //       .orderBy("timestamp", "desc")
  //       .onSnapshot((snapshot) => {
  //         setMessages(snapshot.docs.map((doc) => doc.data()));
  //       });
  //   }
  // }, [id]);

  useEffect(() => {
    setSeed(Math.floor(Math.random() * 5000));
  }, []);

  // const createChat = () => {
  //   const roomName = prompt("Please enter a name for the chat room");
  //   if (roomName) {
  //     //do clever firebase db
  //     db.collection("rooms").add({
  //       name: roomName,
  //     });
  //   }
  // };

  return !addNewChat ? (
    <Link to={`/rooms/${id}`}>
      <div className="sidebarChat">
        <Avatar
          src={`https://avatars.dicebear.com/api/human/${seed}.svg`}
          className={classes.large}
        />
        <div className="sidebarChat__info">
          <h3>{name}</h3>
          {/* <small>{messages[0]?.message}</small> */}
        </div>
      </div>
    </Link>
  ) : (
    <div onClick={()=>{}} className="sidebarChat">
      <h2>Add new Chat</h2>
    </div>
  );
}

export default SidebarChat;
