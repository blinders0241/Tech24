import { useEffect, useState, useRef } from "react";
import axios from "axios";
import Container from "react-bootstrap/Container";

const Youtube = () => {
    const [videoId, setVideoId] = useState("dQw4w9WgXcQ");
    const [inputValue, setInputValue] = useState("");
    const allNotesapi = "http://127.0.0.1:8000/farFlix/";

    const options = [
        "720",
        "480",
        "360",
        "240",
        "144"
    ];
    const index = useRef(0);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.get(`${allNotesapi}FF_Youtube/`, {
                params: {
                    videoId: inputValue,
                },
              });
            console.log(response); // Add this line to print the response received

        } catch (error) {
            // Handle the error as needed
        }
    };

    useEffect(() => {
        const interval = setInterval(() => {
            index.current = (index.current + 1) % options.length;
            setVideoId(options[index.current]);
        }, 90000);
        return () => clearInterval(interval);
    }, [videoId]);

    return (
        <div className="container" style={{ backgroundImage: "url('path/to/background/image.jpg')" }}>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <textarea className="form-control" style={{ height: "200px", width: "400px" }} value={inputValue} onChange={(e) => setInputValue(e.target.value)} />
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
            {/* Rest of the component */}
        </div>
    );
};

export default Youtube;
