import TitleBar from "../TitleBar/TitleBar";
import ReactMarkdown from "react-markdown";
import { useMarkdown } from "../../providers/markdown-provider";
import { styled } from "@mui/system";
import "./preview.css";

const PreviewDiv = styled("div")({
  height: "800px",
  color: "black",
  backgroundColor: "white",
  marginTop: "20px",
  marginLeft: "1px",
  fontSize: "16px",
  fontFamily: "Cambria",
  textAlign: "left",
  padding: "5px",
});

const Preview = () => {
  const [markdown] = useMarkdown();
  console.log(markdown);

  return (
    <>
      <PreviewDiv>
        <ReactMarkdown>{markdown}</ReactMarkdown>
      </PreviewDiv>
    </>
  );
};

export default Preview;
