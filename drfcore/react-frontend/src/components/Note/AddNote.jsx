import React, { useRef } from "react";
import { Container } from "react-bootstrap";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Link } from "react-router-dom";
import { margin } from "@mui/system";

const AddNote = ({
  handleFormSubmit,
  title,
  setTitle,
  tags,
  setTags,
  reactions,
  setReactions,
  body,
  setBody,
}) => {
  console.log("Length of the Notes", body.length);
  // console.log("ALI");
  const inputRef = useRef();

  return (
    <>
      <Container>
        <form onSubmit={handleFormSubmit}>
          <Row className="justify-content-md-center">
            <Col md={{ span: 8 }}>
              <input
                id="title"
                type="text"
                onChange={(e) => setTitle(e.target.value)}
                autoFocus={true}
                ref={inputRef}
                required={true}
                class="form-control"
                value={title}
                placeholder="Title goes here ..."
              />
            </Col>
          </Row>
          <Row className="justify-content-md-center">
            <Col md={{ span: 4 }}>
              <select
                id={reactions}
                value={reactions}
                onChange={(e) => setReactions(e.target.value)}
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
            </Col>
            <Col md={{ span: 4 }}>
              <input
                id="tags"
                type="text"
                onChange={(e) => setTags(e.target.value)}
                ref={inputRef}
                required={true}
                value={tags}
                placeholder="tags"
                class="form-control"
              />
            </Col>
          </Row>
          <Row className="justify-content-md-center">
            <Col md={{ span: 8 }}>
              <input class="form-check-input" type="checkbox" id="gridCheck" />
              <label class="form-check-label" for="gridCheck">
                Todo Item?
              </label>
            </Col>
          </Row>
          <Row className="justify-content-md-center">
            <Col md={{ span: 8 }}>
              <textarea
                class="form-control"
                id="body"
                rows="20"
                onChange={(e) => setBody(e.target.value)}
                value={body}
                required={true}
                placeholder="Add your Next Note.."
              ></textarea>
            </Col>{" "}
          </Row>
          <Row className="justify-content-md-center">
            <Col md={{ span: 2 }}>
              <button
                type="submit"
                class="btn btn-primary"
                onClick={(e) => inputRef.current.focus()}
              >
                Add Note
              </button>
              <Link to={`/`}>
                <button class="btn btn-primary">Home</button>
              </Link>
            </Col>
          </Row>
        </form>
      </Container>
    </>
  );
};

export default AddNote;
