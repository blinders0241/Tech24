import ActualNotes from "./ActualNotes";
import { Container, Row, Col } from "react-bootstrap";
const NoteMapper = ({ note }) => {
  return (
    <>
      {note.length > 0 ? (
        <Container fluid>
          <Row style={{ marginLeft: "5px" }}>
            {note.map((note, index) => (
              <Col md={4} key={note.id}>
                <ActualNotes note={note} />
              </Col>
            ))}
          </Row>
        </Container>
      ) : (
        <div className="empty">
          <h2>No Notes Found!</h2>
          <p>There are no notes found with this keyword</p>
        </div>
      )}
    </>
  );
};

export default NoteMapper;
