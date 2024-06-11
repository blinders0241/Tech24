import { useState, useEffect } from "react";
import { Routes, Route, useNavigate } from "react-router-dom";
// All Page Imports
import Header from "./components/Header/Header";
//Note Applications Improt
import AddNote from "./components/Note/AddNote";
import ViewNotes from "./components/Note/ViewNotes";
import NotePage from "./components/Note/NotePage";
import EditNote from "./components/Note/EditNote";
import MainLayout from "./components/MainLayout/MainLayout";
import Editor from "./components/MarkDownEditor/editor";
import Preview from "./components/MarkDownPreview/preview";
import MarkdownProvider from "./providers/markdown-provider";
//External Imports
import axios from "axios";
import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container } from "react-bootstrap";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

// import SideBar from "./components/Note/NotesSideBar";
import UploadBhavCopy from "./components/RealIT/Upload/UploadBhavCopy";
import DisplayFutures from "./components/RealIT/Display/DisplayFutures";
// import DisplayIndexFutures from "./components/RealIT/Display/DisplayIndexFutures";

import UploadEquityBhavCopy from "./components/RealIT/Upload/UploadEquityBhavCopy";
import DisplayEquity from "./components/RealIT/Display/DisplayEquity";
import FarFlixhome from "./components/FarFlix/FarFlixhome";
import NoteHome from "./components/Note/NoteHome";
import FarFlixUpload from "./components/FarFlix/FarFlixUpload";
import FarFlixSearch from "./components/FarFlix/FarFlixSearch";
// import OpenVlcPlayer from "./components/FarFlix/OpenVlcPlayer";
import FFMovieDetailsUpload from "./components/FarFlix/FFMovieDetailsUpload";
import FFEditDBDetails from "./components/FarFlix/FFEditDBDetails";
import SparrowLive from "./components/LiveSparrow/SparrowLive";
import DisplayNotes from "./components/Note/Display/DisplayNotes";
import DIsplayMarkDown from "./components/MarkDownPreview/DIsplayMarkDown";
import HeatMap from "./components/RealIT/Display/HeatMap";
import Weather from "./components/Weather/Weather";
import UploadIndexHistoricals from "./components/RealIT/Upload/UploadIndexHistoricals";
import IndexMeter from "./components/RealIT/Display/IndexCorner/IndexMeter";
import DisplayIndexFutures from "./components/RealIT/Display/IndexCorner/DisplayIndexFutures";

const allNotesapi = "http://127.0.0.1:8000/api/home/";

function App() {
  const [note, setNote] = React.useState([]);
  const [isLoading, setisLoading] = useState(true);
  const [title, setTitle] = useState("");
  const [tags, setTags] = useState("");
  const [reactions, setReactions] = useState("");
  const [body, setBody] = useState("");
  const [editTitle, setEditTitle] = useState("");
  const [editTags, setEditTags] = useState("");
  const [editReactions, setEditReactions] = useState("");
  const [editBody, setEditBody] = useState("");

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get(allNotesapi);
      // Sort the data by the date field
      const sortedData = response.data.sort(
        (a, b) => b.id.valueOf() - a.id.valueOf()
      );

      setNote(sortedData);
      setisLoading(false);
    } catch (error) {
      console.log(error);
    }
  };
  const history = useNavigate();

  const handleNoteSubmit = async () => {
    // console.log("Initial Note ", note);
    const id = note.length > 0 ? note[note.length - 1].id + 1 : 1;
    const newNote = {
      id: id,
      title: title,
      tags: tags,
      reactions: reactions,
      body: body,
    };
    console.log("NEW NOTE to be added", newNote);
    try {
      await axios.post(allNotesapi, newNote);
    } catch (error) {
      console.log(error);
    }
    fetchData();
    history("/");
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/home/${id}/`);
      const newList = note.filter((todo) => todo.id !== id);
      setNote(newList);
    } catch (error) {
      console.log(error);
    }
    history("/");
  };

  const handleUpdate = async (id) => {
    const updatedNote = {
      id: id,
      title: editTitle,
      tags: editTags,
      reactions: editReactions,
      body: editBody,
    };

    // Display the number of characters in the body and the maximum limit
    console.log(`Body length: ${updatedNote.body.length} / 4000 chars`);

    if (updatedNote.body.length >= 4000) {
      console.log(
        `Body exceeds the max limit. Received Body: ${updatedNote.body.length}, Allowed: 4000 chars`
      );
      return; // Return early to prevent further execution
    }

    try {
      // Make the API call inside a try-catch block to handle potential errors
      const response = await axios.patch(
        `http://127.0.0.1:8000/api/home/${id}/`,
        updatedNote
      );

      // Check if the update was successful
      if (response.status === 200) {
        console.log("Update successful");
        fetchData();
        setEditBody("");
        setEditTitle("");
        setEditTags("");
        setEditReactions("");
        // Navigate to the updated note instead of home
        history(`/home/${id}`);
      } else {
        console.log("Update failed");
      }
    } catch (error) {
      console.log(error);
    }
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    if (!title && !description) return;
    handleNoteSubmit();
  };

  return (
    <>
      {/* <div class="container-fluid"> */}
      <Container fluid>
        <Row>
          <Col>
            <Header />
          </Col>
        </Row>
        <Row>
          <Routes>
            {/* Routes to Home to view notes*/}
            <Route path="/" element={<ViewNotes note={note} />}></Route>
            {/* Routes to add new Notes */}
            <Route
              path="/notes"
              element={
                <AddNote
                  handleFormSubmit={handleFormSubmit}
                  title={title}
                  setTitle={setTitle}
                  tags={tags}
                  setTags={setTags}
                  reactions={reactions}
                  setReactions={setReactions}
                  body={body}
                  setBody={setBody}
                />
              }
            ></Route>
            {/* Routes to indivual Notes */}
            <Route
              path="/edit/:id"
              element={
                <EditNote
                  editTitle={editTitle}
                  setEditTitle={setEditTitle}
                  editTags={editTags}
                  setEditTags={setEditTags}
                  editBody={editBody}
                  setEditBody={setEditBody}
                  setEditReactions={setEditReactions}
                  editReactions={editReactions}
                  handleUpdate={handleUpdate}
                  note={note}
                />
              }
            ></Route>
            {/* Routes to Delete Note */}
            <Route
              path="/home/:id/"
              element={<NotePage note={note} handleDelete={handleDelete} />}
            ></Route>

            <Route path="/displayNotes" element={<DisplayNotes />}></Route>
            <Route
              path="/markdown/:id/"
              element={<DIsplayMarkDown notes={note} />}
            ></Route>
            {/* Routes to MarkDown Area */}
            <Route
              path="/markdown"
              element={
                <MarkdownProvider>
                  <MainLayout>
                    <MainLayout.Column>
                      <Editor />
                    </MainLayout.Column>
                    <MainLayout.Column>
                      <Preview />
                    </MainLayout.Column>
                  </MainLayout>
                </MarkdownProvider>
              }
            />
            {/* RealiTY : (Real IT solution for Generation Y, also known as Millennials)  */}
            {/* Routes to upload bhavCopy */}
            <Route path="/uploadData" element={<UploadBhavCopy />}></Route>
            <Route
              path="/UploadIndexHistoricals"
              element={<UploadIndexHistoricals />}
            ></Route>
            <Route
              path="/uploadequity"
              element={<UploadEquityBhavCopy />}
            ></Route>
            {/* Routes to display Stock Futures Data */}
            <Route
              path="/displayStockdetails"
              element={<DisplayFutures />}
            ></Route>
            <Route
              path="/displayEquityetails"
              element={<DisplayEquity />}
            ></Route>
            <Route
              path="/displayIndexdetails"
              element={<DisplayIndexFutures />}
            />
            {/* Section for FarFlix */}
            {/* <Route path="/FarFlixhome" element={<OpenVlcPlayer />}></Route> */}
            <Route path="/FarFlixUpload" element={<FarFlixUpload />}></Route>
            <Route
              path="/FFMovieDetailsUpload"
              element={<FFMovieDetailsUpload />}
            ></Route>
            <Route
              path="/FF_FetchEditDetailsTODB"
              element={<FFEditDBDetails />}
            ></Route>
            <Route path="/FarFlixSearch" element={<FarFlixSearch />}></Route>
            <Route path="/sparrowHome" element={<SparrowLive />}></Route>
            <Route path="/heatMap" element={<HeatMap />}></Route>
            <Route path="/Weather" element={<Weather />}></Route>
            <Route path="/IndexMeter" element={<IndexMeter />}></Route>
          </Routes>
        </Row>
      </Container>
      {/* </div> */}
    </>
  );
}

export default App;
