import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css";
import "ag-grid-community/styles/ag-theme-alpine.css";
import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";

import React, { useState } from "react";
import { useEffect } from "react";
import axios from "axios";
import { NotesColDef } from "../../ColumnViews/NotesColDef";
import DetailsNotes from "./DetailsNotes";
import { Typography } from "@mui/material";

const DisplayNotes = () => {
  const [note, setNote] = React.useState([]);
  const [noteCreated, setnoteCreated] = React.useState([]);
  const [noteBody, setnoteBody] = React.useState(
    "Your notes will be displayed here!.."
  );
  const [noteTitle, setnoteTitle] = React.useState([]);
  const [noteTags, setnoteTags] = React.useState([]);
  const [gridApi, setGridApi] = useState(null);

  const allNotesapi = "http://127.0.0.1:8000/api/home/";
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
      console.log(sortedData);
    } catch (error) {
      console.log(error);
    }
  };

  const onSelectionChanged = (params) => {
    const selectedNodes = params.api.getSelectedNodes();
    selectedNodes.forEach((node) => {
      console.log(node.data);
      setnoteCreated(node.data.created);
      setnoteBody(node.data.body);
      setnoteTitle(node.data.title);
      setnoteTags(node.data.tags);
    });
  };

  const onCellDoubleClicked = (params) => {
    navigator.clipboard.writeText(params.value);
    alert("Copied: " + params.value);
  };
  const onGridReady = (params) => {
    setGridApi(params.api);
    setGridColumnApi(params.columnApi);
    // Sort the data in descending order of dates on load
    params.columnApi.applyColumnState({
      state: [{ colId: "updated", sort: "desc" }],
      defaultState: { sort: null },
    });
  };
  const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === "dark" ? "#1A2027" : "#fff",
    ...theme.typography.body2,
    padding: theme.spacing(1),
    // textAlign: "center",
    color: theme.palette.text.secondary,
  }));

  return (
    <>
      <Box sx={{ flexGrow: 1 }}>
        <Grid container spacing={1}>
          <Grid item xs={6} md={5}>
            {/* <Item> */}
            <div
              style={{ height: "880px", width: "100%" }}
              className="ag-theme-alpine"
            >
              <AgGridReact
                onGridReady={onGridReady}
                rowData={note}
                columnDefs={NotesColDef}
                pagination={true}
                rowSelection="single" // Enable multiple row selection
                onSelectionChanged={onSelectionChanged}
                onCellDoubleClicked={onCellDoubleClicked}
              />
            </div>
            {/* </Item> */}
          </Grid>
          <Grid item xs={6} md={7}>
            <Item>
              <Typography variant="h6" align="center" gutterBottom>
                {noteTitle}
              </Typography>
              <Typography variant="subtitle1" gutterBottom>
                <div className="full-notes">
                  <div className="description text-primary">
                    <p className="text-left">{noteBody}</p>
                  </div>
                </div>
              </Typography>
            </Item>
          </Grid>
        </Grid>
      </Box>
    </>
  );
};
export default DisplayNotes;
