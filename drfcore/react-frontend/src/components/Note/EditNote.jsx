import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { useEffect } from "react";

const EditNote = ({
  note,
  handleUpdate,
  setEditTitle,
  editTitle,
  setEditBody,
  editBody,
  setEditReactions,
  editReactions,
  editTags,
  setEditTags,
}) => {
  const { id } = useParams();
  const post = note.find((note) => note.id.toString() === id);
  // console.log(post.body.length);

  useEffect(() => {
    if (post) {
      setEditTitle(post.title);
      setEditTags(post.tags);
      setEditBody(post.body);
      setEditReactions(post.reactions);
    }
  }, []);

  return (
    <div>
      <form onSubmit={(e) => e.preventDefault()}>
        <div class="form-row">
          <div class="form-group col-md-10">
            <input
              id="title"
              type="text"
              onChange={(e) => setEditTitle(e.target.value)}
              autoFocus={true}
              required={true}
              class="form-control"
              value={editTitle}
              placeholder="Title goes here ..."
            />
          </div>
        </div>

        <div class="form-group col-md-4">
          <select
            id={editReactions}
            value={editReactions}
            onChange={(e) => setEditReactions(e.target.value)}
            defaultValue="Generic"
            class="form-control"
          >
            <option value="Generic">Generic</option>
            <option value="Work">Work</option>
            <option value="Personal">Personal</option>
            <option value="Learnings">Learnings</option>
            <option value="Finance">Finance</option>
            <option value="Archive">Archive</option>
          </select>
        </div>

        <div class="row">
          <div class="form-group col-md-6">
            <label for="tags">Tags</label>
            <input
              id="tags"
              type="text"
              onChange={(e) => setEditTags(e.target.value)}
              required={true}
              value={editTags}
              placeholder="tags"
              class="form-control"
            />
          </div>
        </div>

        <div class="row">
          <div class="form-group col-md-10">
            <textarea
              class="form-control"
              id="body"
              rows="20"
              onChange={(e) => setEditBody(e.target.value)}
              value={editBody}
              required={true}
              placeholder="Add your Next Note.."
            ></textarea>
          </div>
        </div>

        <div class="form-group row">
          <div class="col-sm-10 m-2">
            <button
              type="submit"
              class="btn btn-primary"
              onClick={() => handleUpdate(post.id)}
            >
              Update Note
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default EditNote;
