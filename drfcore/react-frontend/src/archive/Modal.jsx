import { motion, AnimatePresence } from "framer-motion";
import React from "react";
import styles from "./Modal.module.css";
import Note from "./Note";

export default function Modal({ post, NoteId }) {
  const postbody = post.find((note) => post.id === NoteId);
  console.log("FIletered", postbody);
  console.log("FIleteredID", NoteId);

  return (
    <motion.div
      className={styles.beutyModal}
      initial={{ opacity: 0 }}
      animate={{
        transform: ["translatex(100px)", "translatex(0px)"],
        opacity: 1,
      }}
      transition={{
        duration: 0.8,
        type: "spring",
        stiffness: 200,
      }}
      exit={{
        opacity: 0,
      }}
    >
      {/* <p>{NoteId}</p> */}
    </motion.div>
  );
}
