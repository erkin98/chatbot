import React from "react";
import "./Sidebar.css";

import SidebarChat from "./SidebarChat";
import { useStateValue } from "./StateProvider";
function Sidebar() {
  const [state] = useStateValue();

  return (
    <div className="sidebar">
      <div className="sidebar__chats">
        {state.customers.map((c,idx)=> <SidebarChat key={`customer-${idx}`} name={c} id={idx}/>)}
      </div>
    </div>
  );
}

export default Sidebar;
