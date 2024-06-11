import NoteMapper from "./NoteMapper";
import NotesSideBar from "./NotesSideBar";
import { useState, useEffect } from "react";
import { Container } from "react-bootstrap";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Link } from "react-router-dom";
import React from "react";
import { TbTransformFilled } from "react-icons/tb";
import { FcSearch } from "react-icons/fc";
import { VscNewFile } from "react-icons/vsc";
import { Alert, Typography } from "@mui/material";

const ViewNotes = ({ note }) => {
  const [isSideButtonClicked, setIsSideButtonClicked] = useState(false);
  const [filterednote, setFilteredNote] = React.useState([]);
  const [searchedNote, setSearchedNote] = useState(note);
  useEffect(() => {
    setSearchedNote(note);
  }, [note]);

  const handleSearch = (e) => {
    setIsSideButtonClicked(false);
    if (e.target.value.trim().length === 0) return setSearchedNote(note);
    const noteArray = note.filter(
      (note) =>
        note.title
          .toLowerCase()
          .includes(e.target.value.toLowerCase().replace(/\s+/g, " ").trim()) ||
        note.body
          .toLowerCase()
          .includes(e.target.value.toLowerCase().replace(/\s+/g, " ").trim())
    );
    setSearchedNote(noteArray);
  };

  const handleButtonClick = (reaction, isSideButtonClicked) => {
    const noteArray2 = note.filter((note) => note.reactions.includes(reaction));
    setFilteredNote(noteArray2);
    setIsSideButtonClicked(isSideButtonClicked);
  };

  return (
    <>
      <Container fluid>
        <Row>
          <Col xs={2}>
            <Typography
              variant="h6"
              component={Link}
              to="/notes"
              sx={{
                textDecoration: "none",
                marginLeft: "22px",
                marginBottom: "32px",
                backgroundColor: "#D7DBDD",
                fontSize: "24px", // text size
              }}
            >
              New Note
            </Typography>
          </Col>
          <Col xs={10}>
            {note && note.length && (
              <div className="search">
                <input
                  type="text"
                  placeholder="search your note here !"
                  autoFocus={true}
                  onChange={(e) => {
                    handleSearch(e);
                  }}
                />
                <Typography
                  variant="h6"
                  component={Link}
                  to="/displayNotes"
                  sx={{
                    textDecoration: "none",
                    letterSpacing: "4px",
                    fontSize: "40px", // text size
                  }}
                >
                  <TbTransformFilled />
                </Typography>
              </div>
            )}
          </Col>
        </Row>
        <Row>
          <Col xs={2}>
            <NotesSideBar note={note} onButtonClick={handleButtonClick} />
          </Col>
          <Col xs={10}>
            {isSideButtonClicked ? (
              <NoteMapper note={filterednote.slice(0, 9)} />
            ) : (
              <NoteMapper note={searchedNote.slice(0, 9)} />
            )}
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default ViewNotes;
