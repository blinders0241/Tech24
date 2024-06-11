import { Container } from "react-bootstrap";
import Badge from "react-bootstrap/Badge";
import Button from "react-bootstrap/Button";

const NotesSideBar = ({ note, onButtonClick }) => {
  let reactionCounts = note.reduce((acc, item) => {
    if (!acc[item.reactions]) {
      acc[item.reactions] = 0;
    }
    acc[item.reactions]++;
    return acc;
  }, {});

  // Convert the reactionCounts object into an array of [reaction, count] pairs
  const reactionsArray = Object.entries(reactionCounts);
  // Sort the array by count in descending order
  const sortedReactions = reactionsArray.sort((a, b) => b[1] - a[1]);
  // console.log(sortedReactions);
  // Define a color for each reaction
  const reactionColors = {
    Finance: "primary",
    Deleted: "danger",
    Archive: "warning",
    Personal: "success",
    Learnings: "warning",
    Work: "dark",
  };

  // Function to handle button click
  const handleClick = (reaction, isSideButtonClicked) => {
    // Call the function passed as a prop
    onButtonClick(reaction, isSideButtonClicked);
    // console.log(reaction);
  };

  return (
    <>
      <Container>
        {sortedReactions.map(([reaction, count]) => (
          <Button
            variant={reactionColors[reaction] || "secondary"}
            key={reaction}
            onClick={() => {
              if (sortedReactions.some(([r]) => r === reaction)) {
                const isSideButtonClicked = true;
                return handleClick(reaction, isSideButtonClicked);
              } else {
                const isSideButtonClicked = false;
                return handleClick(reaction, isSideButtonClicked);
              }
            }}
            // onClick={() => handleClick(reaction , )} // Add onClick event handler
            style={{
              margin: "5px",
              border: "none",
              fontSmooth: true,
              fontSize: "medium",
            }}
          >
            {reaction}{" "}
            <Badge
              bg="light"
              style={{ marginLeft: "10px", fontSize: "large", color: "black" }}
            >
              {count}
            </Badge>
            <span className="visually-hidden">count</span>
          </Button>
        ))}
      </Container>
    </>
  );
};
export default NotesSideBar;
