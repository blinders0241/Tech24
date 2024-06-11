import TitleBar from "../TitleBar/TitleBar";
import ReactMarkdown from "react-markdown";
import { useMarkdown } from "../../providers/markdown-provider";

import { useParams } from "react-router-dom";
import "./preview.css";
import { styled } from "@mui/system";
const PreviewDiv = styled("div")({
  color: "black",
  backgroundColor: "white",
  marginTop: "20px",
  marginLeft: "1px",
  fontSize: "16px",
  fontFamily: "Cambria",
  textAlign: "left",
  padding: "5px",
});

const DIsplayMarkDown = ({ notes }) => {
  const { id } = useParams();
  if (!notes) {
    console.log("notes is undefined");
    return <div>Error: notes is undefined</div>;
  }
  const note = notes.find((note) => String(note.id) === String(id));
  if (!note) {
    console.log(`No note found with id ${id}`);
    return <div>Error: No note found with the given id</div>;
  }

  // console.log(note);

  return (
    <PreviewDiv>
      <ReactMarkdown>{note.body}</ReactMarkdown>
    </PreviewDiv>
  );
};

export default DIsplayMarkDown;
