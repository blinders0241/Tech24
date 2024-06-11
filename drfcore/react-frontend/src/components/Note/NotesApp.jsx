import React, { useState } from "react";

const Note = ({ note }) => <li>{note}</li>;

const NotesApp = () => {
  const [showBusiness, setShowBusiness] = useState(false);
  const [showPersonal, setShowPersonal] = useState(false);
  const [showArchive, setShowArchive] = useState(false);

  const businessNotes = ["Business Note 1", "Business Note 2"];
  const personalNotes = ["Personal Note 1", "Personal Note 2"];
  const archiveNotes = ["Archived Note 1", "Archived Note 2"];

  return (
    <div>
      <button onClick={() => setShowBusiness(!showBusiness)}>
        Toggle Business Notes
      </button>
      <button onClick={() => setShowPersonal(!showPersonal)}>
        Toggle Personal Notes
      </button>
      <button onClick={() => setShowArchive(!showArchive)}>
        Toggle Archived Notes
      </button>

      {showBusiness && (
        <div>
          <h2>Business Notes</h2>
          <ul>
            {businessNotes.map((note, index) => (
              <Note key={index} note={note} />
            ))}
          </ul>
        </div>
      )}

      {showPersonal && (
        <div>
          <h2>Personal Notes</h2>
          <ul>
            {personalNotes.map((note, index) => (
              <Note key={index} note={note} />
            ))}
          </ul>
        </div>
      )}

      {showArchive && (
        <div>
          <h2>Archived Notes</h2>
          <ul>
            {archiveNotes.map((note, index) => (
              <Note key={index} note={note} />
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default NotesApp;
