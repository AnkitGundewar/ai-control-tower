import { useState } from "react";

import {
  Paper,
  Box,
  TextField,
  Button,
  Typography,
  CircularProgress,
} from "@mui/material";

import api from "../../services/api";
import { useShipmentContext } from "../../context/useShipmentContext";

export default function ChatPanel() {
  const { selectedShipment } = useShipmentContext();

  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function askAI() {
    if (
      loading ||
      !selectedShipment ||
      !question.trim()
    ) {
      return;
    }

    const userQuestion = question.trim();

    setMessages((previous) => [
      ...previous,
      {
        role: "user",
        text: userQuestion,
      },
    ]);

    setQuestion("");
    setLoading(true);

    try {
      const result = await api.post(
        "/ai/chat",
        {
          request_id: crypto.randomUUID(),
          correlation_id: crypto.randomUUID(),
          session_id: crypto.randomUUID(),
          user_role: "operator",
          shipment_ids: [
            selectedShipment.shipmentId,
          ],
          payload: {
            question: userQuestion,
          },
        }
      );

      console.log("Shipment AI Response");
      console.log(result.data);

      if (!result.data.success) {
        throw new Error(
          result.data.errors?.[0]?.message ??
            "Unknown AI error."
        );
      }

      const answer =
        result.data.payload?.answer ??
        "No response returned.";

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          text:
            typeof answer === "string"
              ? answer
              : JSON.stringify(answer, null, 2),
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          text:
            error.message ??
            "Unable to retrieve an AI response.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <Paper
      sx={{
        height: 320,
        p: 3,
        display: "flex",
        flexDirection: "column",
        gap: 2,
      }}
    >
      <Typography variant="h6">
        🤖 Shipment AI
      </Typography>

      <TextField
        fullWidth
        multiline
        minRows={2}
        placeholder={
          selectedShipment
            ? "Ask a question about the selected shipment..."
            : "Select a shipment first..."
        }
        value={question}
        disabled={!selectedShipment || loading}
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
        onClick={askAI}
        disabled={
          loading ||
          !selectedShipment ||
          !question.trim()
        }
      >
        Ask AI
      </Button>

      <Box
        sx={{
          flex: 1,
          overflowY: "auto",
          border: "1px solid #ddd",
          borderRadius: 1,
          p: 2,
          bgcolor: "#fafafa",
        }}
      >
        {messages.length === 0 && !loading && (
          <Typography color="text.secondary">
            Ask a question about the selected shipment.
          </Typography>
        )}

        {messages.map((message, index) => (
          <Box key={index} sx={{ mb: 2 }}>
            <Typography
              variant="subtitle2"
              fontWeight="bold"
            >
              {message.role === "user"
                ? "You:"
                : "Assistant:"}
            </Typography>

            <Typography variant="body2">
              {typeof message.text === "string"
                ? message.text
                : JSON.stringify(
                    message.text,
                    null,
                    2
                  )}
            </Typography>
          </Box>
        ))}

        {loading && (
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              mt: 2,
            }}
          >
            <CircularProgress size={24} />
          </Box>
        )}
      </Box>
    </Paper>
  );
}