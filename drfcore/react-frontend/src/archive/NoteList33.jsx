import { useContext, useEffect, useState } from "react";
import React from "react";
import Note from "./Note";
import axios from "axios";

const allNotesapi = "http://127.0.0.1:8000/api/home/";

function NoteList() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    axios.get(allNotesapi).then((response) => {
      setPost(response.data);
    });
  }, []);

  if (!post) return null;

  return (
    <div>
      <Note post={post}></Note>
    </div>
  );
}

export default NoteList;
