import React from "react";
import "./Sidebar.css";
import { IconButton } from "@material-ui/core";
import DonutLargeIcon from "@material-ui/icons/DonutLarge";
import ChatIcon from "@material-ui/icons/Chat";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import { SearchOutlined } from "@material-ui/icons";
import SidebarChat from "./SidebarChat";
import { useStateValue } from "./StateProvider";
function Sidebar() {
  const [state, dispatch] = useStateValue();

  return (
    <div className="sidebar">
      <div className="sidebar__header">
        <div className="header__userInfo">
          {/* <Avatar src={state?.user?.additionalUserInfo?.profile?.picture} /> */}
          {/* <p>{state.user.user.displayName}</p> */}
        </div>
        <div className="sidebar__headerRight">
          <IconButton>
            <DonutLargeIcon />
          </IconButton>
          <IconButton>
            <ChatIcon />
          </IconButton>
          <IconButton>
            <MoreVertIcon />
          </IconButton>
        </div>
      </div>
      <div className="sidebar__search">
        <SearchOutlined />
        <input type="text" placeholder="Search or start new chat" />
      </div>
      <div className="sidebar__chats">
        {/* <SidebarChat addNewChat /> */}
        {state.customers.map((c,idx)=> <SidebarChat key={`customer-${idx}`} name={c} id={idx}/>)}
      </div>
    </div>
  );
}

export default Sidebar;
