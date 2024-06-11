import React from "react";
import { format } from "date-fns";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import { FaArrowUpRightFromSquare } from "react-icons/fa6";
import { BiSolidEdit } from "react-icons/bi";
import { styled } from "@mui/system";
import Alert from "react-bootstrap/Alert";
import Card from "react-bootstrap/Card";
import { Typography } from "@mui/material";
import { IoLogoMarkdown } from "react-icons/io5";

const ActualNotes = ({ note }) => {
  const noteCreatedTime = format(note.created, "MMMM dd, yyyy pp");

  const PreviewDiv = styled("div")({
    color: "black",
    backgroundColor: "#D7DBDD",
    fontSize: "14px",
    textAlign: "left",
    border: "1px solid black",
    padding: "5px",
    textDecoration: "none",
    letterSpacing: "4px",
  });
  const LinkBox = styled("div")({
    color: "white",
    backgroundColor: "#EEFBE2",
    fontSize: "26px",
    textAlign: "left",
    border: "1px solid black",
    padding: "5px",
    textDecoration: "none",
  });
  return (
    <Card style={{ height: "280px", marginBottom: "10px" }}>
      <Card.Header>
        <b>{note.reactions}</b> | {noteCreatedTime}
      </Card.Header>
      <Card.Body>
        <Card.Title>{note.title.slice(0, 64)}</Card.Title>

        <PreviewDiv>{note.tags}</PreviewDiv>
        <LinkBox>
          <Link to={`/edit/${note.id}`}>
            <BiSolidEdit />
          </Link>
          <Typography
            variant="h6"
            component={Link}
            to={`/edit/${note.id}`}
            sx={{
              marginLeft: "12px",
              marginRight: "24px",
              fontSize: "36px", // text size
            }}
          >
            <BiSolidEdit />
          </Typography>
          <Typography
            variant="h6"
            component={Link}
            to={`/home/${note.id}`}
            sx={{
              marginLeft: "12px",
              fontSize: "20px", // text size
            }}
          >
            <FaArrowUpRightFromSquare />
          </Typography>
          <Typography
            variant="h6"
            component={Link}
            to={`/markdown/${note.id}`}
            sx={{
              marginLeft: "12px",
              fontSize: "24px", // text size
            }}
          >
            <IoLogoMarkdown />{" "}
          </Typography>
        </LinkBox>

        {/* <hr></hr> */}
      </Card.Body>

      {/* <Card.Text> */}
    </Card>
  );
};

export default ActualNotes;
