const FarFlixhome = () => {
  const handleSearch = (e) => {
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

  return (
    <>
      <h1>FarFlix Home</h1>
      <div className="notesArea">
        <div className="search">
          <input
            type="text"
            placeholder="search your Movies here !"
            autoFocus={true}
            onChange={(e) => {
              handleSearch(e);
            }}
          />
        </div>
      </div>
    </>
  );
};

export default FarFlixhome;
