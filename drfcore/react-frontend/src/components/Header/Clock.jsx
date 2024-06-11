import React, { useState, useEffect } from "react";
import axios from "axios"; // Import axios library
import useSound from "use-sound";
import alertSound from "./azan1.mp3"; // replace this with the path to your sound file

function Clock() {
  const [time, setTime] = useState(new Date());
  const [nextPrayer, setNextPrayer] = useState("");
  const [todayPrayerTimes, setTodayPrayerTimes] = useState({}); // Initialize as an empty object
  const city = "Kolkata";
  const [play] = useSound(alertSound);

  useEffect(() => {
    const timerID = setInterval(() => {
      setTime(new Date());
    }, 1000); // Update every second

    // Cleanup on unmount
    return () => {
      clearInterval(timerID);
    };
  }, []);

  useEffect(() => {
    const fetchPrayerTimes = async () => {
      try {
        const response = await axios.get(
          "https://muslimsalat.p.rapidapi.com/" + city + ".json",
          {
            headers: {
              "X-RapidAPI-Key":
                "rvv2Kc4YzLmshnr5Lv4cBZxYILPIp1sdfDGjsngKgtiHwTomE7",
              "X-RapidAPI-Host": "muslimsalat.p.rapidapi.com",
            },
          }
        );

        const { data } = response;
        const todayPrayerTimes = data.items[0]; // Get today's prayer times
        setTodayPrayerTimes(todayPrayerTimes); // Set the prayer times state

        // Calculate the next prayer time
        const currentTime = time.getTime();
        const prayerKeys = Object.keys(todayPrayerTimes);

        for (let i = 0; i < prayerKeys.length; i++) {
          const prayerTime = new Date(
            new Date().toDateString() + " " + todayPrayerTimes[prayerKeys[i]]
          );
          const timeDiff = prayerTime.getTime() - currentTime;

          if (timeDiff > 0) {
            setNextPrayer(prayerKeys[i]);
            break;
          }
        }
        // If the current time matches the prayer time, play the alert sound
        if (
          nextPrayer &&
          time.toLocaleTimeString() === todayPrayerTimes[nextPrayer]
        ) {
          console.log("Prayer TIME");
          play();
        }
      } catch (error) {
        console.error("Error fetching prayer times:", error);
      }
    };

    fetchPrayerTimes();
  }, [time]);

  // Calculate remaining time in hours and minutes
  const remainingTime = nextPrayer
    ? Math.floor(
        (new Date(
          new Date().toDateString() + " " + todayPrayerTimes[nextPrayer]
        ).getTime() -
          time.getTime()) /
          (60 * 1000)
      )
    : 0;
  const remainingHours = Math.floor(remainingTime / 60);
  const remainingMinutes = remainingTime % 60;

  return (
    <div>
      <h2 style={{ fontSize: "24px", fontWeight: "bold", color: "#2596be" }}>
        {time.toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
        })}
      </h2>
      {nextPrayer && (
        <p>
          Next: {nextPrayer.toUpperCase()} (in {remainingHours} hrs{" "}
          {remainingMinutes} mins)
        </p>
      )}
    </div>
  );
}

export default Clock;
