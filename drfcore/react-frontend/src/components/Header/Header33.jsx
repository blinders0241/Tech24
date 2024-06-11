import { React, useRef } from "react";
import { Link } from "react-router-dom";
import { FcHome } from "react-icons/fc";
import { MdNoteAdd } from "react-icons/md";

// import "../../src/App.css";

const Header = () => {
  return (
    <div className="header">
      <Link to="/">
        <h1></h1>
        <FcHome />
        <p>Home</p>
      </Link>

      <Link to="/notes">
        <MdNoteAdd />
        <p>AddNote</p>
      </Link>

      <Link to="/markdown">
        <p>MarkDown</p>
      </Link>

      <Link to="/uploadData">
        <p>UploadBhavCopy</p>
      </Link>
      <Link to="/displayStockdetails">
        <p>DisplayFutures</p>
      </Link>
    </div>
  );
};

export default Header;
