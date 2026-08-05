import { useState } from "react";

import {
  Paper,
  Typography,
  Box,
  TextField,
  Button,
  CircularProgress,
} from "@mui/material";

import api from "../../services/api";

export default function GlobalChatPanel() {

  const [question, setQuestion] = useState("");

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);

  async function askAI() {

    if (!question.trim()) {
      return;
    }

    setLoading(true);

    try {

      const result = await api.post(
        "/ai/gchat",
        {
          request_id: crypto.randomUUID(),
          correlation_id: crypto.randomUUID(),
          session_id: crypto.randomUUID(),
          user_role: "operator",
          shipment_ids: [],
          payload: {
            question,
          },
        }
      );

      setMessages((previous) => [
        ...previous,
        {
          role: "user",
          text: question,
        },
        {
          role: "assistant",
          text: result.data.answer??
                result.data.payload?.answer ??
                "No response returned.",
        },
      ]);

      setQuestion("");

    } catch {

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          text: "Unable to retrieve a response.",
        },
      ]);

    } finally {

      setLoading(false);

    }

  }

  return (

    <Paper
      elevation={3}
      sx={{
        p: 3,
        height: 200,
        display: "flex",
        flexDirection: "column",
      }}
    >

      <Typography
        variant="h6"
        gutterBottom
      >
        Global Supply Chain AI
      </Typography>

      <Box
        sx={{
          flex: 1,
          overflowY: "auto",
          border: "1px solid #ddd",
          borderRadius: 1,
          p: 2,
          bgcolor: "#fafafa",
          mb: 2,
        }}
      >

        {loading ? (

          <Box
            display="flex"
            justifyContent="center"
            mt={2}
          >
            <CircularProgress
              size={24}
            />
          </Box>

        ) : messages.length === 0 ? (

          <Typography
            color="text.secondary"
          >
            Ask questions about your overall supply chain.
          </Typography>

        ) : (

          messages.map((message, index) => (

            <Box
              key={index}
              sx={{
                mb: 2,
              }}
            >

              <Typography
                fontWeight={600}
              >
                {message.role === "user"
                  ? "You"
                  : "AI"}
              </Typography>

              <Typography
                variant="body2"
              >
                {message.text}
              </Typography>

            </Box>

          ))

        )}

      </Box>

      <Box
        sx={{
          display: "flex",
          gap: 2,
        }}
      >

        <TextField
          fullWidth
          placeholder="Ask about today's supply chain..."
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
          onKeyDown={(e) => {
            if (
              e.key === "Enter" &&
              !e.shiftKey
            ) {
              e.preventDefault();
              askAI();
            }
          }}
        />

        <Button
          variant="contained"
          disabled={
            loading ||
            !question.trim()
          }
          onClick={askAI}
        >
          Send
        </Button>

      </Box>

    </Paper>

  );

}