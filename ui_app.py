import { useState } from "react";
import { Button, Input } from "@/components/ui";

export default function FridayUI() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;
    const res = await fetch("http://localhost:5000/api/friday", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: input }),
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div className="flex flex-col items-center p-4">
      <h1 className="text-2xl font-bold mb-4">FRIDAY AI</h1>
      <div className="w-full max-w-md flex gap-2">
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask FRIDAY..."
        />
        <Button onClick={handleSend}>Send</Button>
      </div>
      {response && (
        <div className="mt-4 p-2 border rounded-lg w-full max-w-md">
          <p className="font-semibold">FRIDAY:</p>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}
