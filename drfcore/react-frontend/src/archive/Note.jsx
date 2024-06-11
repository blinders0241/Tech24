import { useContext, useState } from "react";
import NoteList from "./NoteList33";

const Notes = ({ post }) => {
  const [isVisible, setIsVisible] = useState(false);
  const [noteID, setnoteID] = useState("");

  function handleOnClick(post) {
    console.log("Check", post.id);
    if (isVisible === false) {
      setIsVisible(true);
      setnoteID(post.id);
    } else {
      setIsVisible(false);
    }
  }

  return (
    <>
      {post.map((post) => (
        <>
          <div className="card">
            <div className="card-header">
              <b>{post.title}</b>
            </div>
            <div className="card-body">
              <h5 className="card-title">Tags : {post.tags}</h5>
              {/* <p className="card-text">{post.body}</p> */}
              <div>
                <button onClick={() => handleOnClick(post)}>Show Notes</button>
              </div>
              <a href="#" className="btn btn-primary">
                <b>{post.reactions}</b>
              </a>
            </div>
          </div>
        </>
      ))}
      {/* <Modal post={post} NoteId={noteID} />; */}
    </>
  );

  // const { deletePost } = useContext(PostListData);
};

export default Notes;
