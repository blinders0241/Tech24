import React from "react";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";

const NotePage = ({ note, handleDelete }) => {
  const { id } = useParams();
  let post = [];
  for (var i = 0; i < note.length; i++) {
    if (note[i].id === Number(id)) {
      post.push(note[i]);
    }
  }

  return (
    <>
      {post.length !== 0 &&
        post.map((post) => (
          <>
            <div className="full-notes">
              <div className="title">
                <h2>{post.title}</h2>
              </div>
              <div className="description text-primary">
                <p className="text-left">{post.body}</p>
              </div>
              <div className="button">
                <button onClick={() => handleDelete(post.id)}>Delete</button>
                <Link to={`/edit/${post.id}`}>
                  <button>Update</button>
                </Link>

                <Link to={`/`}>
                  <button>Home</button>
                </Link>
              </div>
            </div>
          </>
        ))}
      {!post && (
        <div className="not-found">
          <h2>Post Not Found</h2>
          <p>Well, that's disappointing.</p>
          <p>
            <Link to="/">Visit Our Homepage</Link>
          </p>
        </div>
      )}
    </>
  );
};

export default NotePage;
