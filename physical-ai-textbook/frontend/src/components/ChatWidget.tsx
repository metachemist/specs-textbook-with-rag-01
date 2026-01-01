import React, { useState, useEffect, useRef } from 'react';
import './ChatWidget.css'; // We'll create this CSS file too

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showTooltip, setShowTooltip] = useState(false);
  const [tooltipPosition, setTooltipPosition] = useState({ x: 0, y: 0 });
  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);

  // Function to handle text selection
  useEffect(() => {
    const handleSelection = () => {
      const selection = window.getSelection();
      if (selection.toString().trim() !== '') {
        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        setTooltipPosition({ x: rect.left, y: rect.top - 10 });
        setShowTooltip(true);
      } else {
        setShowTooltip(false);
      }
    };

    document.addEventListener('mouseup', handleSelection);
    return () => {
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  // Function to scroll to bottom of messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const toggleChat = () => {
    setIsOpen(!isOpen);
    if (!isOpen && textareaRef.current) {
      setTimeout(() => textareaRef.current.focus(), 100);
    }
  };

  const handleSend = async () => {
    if (!inputValue.trim() || isLoading) return;

    // Add user message
    const userMessage = { id: Date.now(), text: inputValue, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Call the backend API
      const response = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          query: inputValue,
          selected_text: null // We could pass selected text here if available
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      // Add AI response
      const aiMessage = { 
        id: Date.now() + 1, 
        text: data.answer, 
        sender: 'ai',
        sources: data.sources || [] 
      };
      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = { 
        id: Date.now() + 1, 
        text: 'Sorry, I encountered an error. Please try again.', 
        sender: 'ai' 
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleAskAI = () => {
    const selection = window.getSelection();
    const selectedText = selection.toString().trim();
    
    if (selectedText) {
      setInputValue(`About this text: "${selectedText}"`);
      setIsOpen(true);
      setShowTooltip(false);
      
      // Clear selection
      window.getSelection().removeAllRanges();
    }
  };

  return (
    <div className="chat-widget">
      {/* Tooltip for selected text */}
      {showTooltip && (
        <div 
          className="text-selection-tooltip"
          style={{ top: tooltipPosition.y, left: tooltipPosition.x }}
          onClick={handleAskAI}
        >
          Ask AI
        </div>
      )}

      {/* Chat widget button */}
      <button 
        className={`chat-button ${isOpen ? 'open' : ''}`}
        onClick={toggleChat}
      >
        {isOpen ? '×' : '💬'}
      </button>

      {/* Chat window */}
      {isOpen && (
        <div className="chat-window">
          <div className="chat-header">
            <h3>AI Textbook Assistant</h3>
          </div>
          
          <div className="chat-messages">
            {messages.length === 0 ? (
              <div className="welcome-message">
                <p>Ask me anything about Physical AI & Humanoid Robotics!</p>
              </div>
            ) : (
              messages.map((message) => (
                <div 
                  key={message.id} 
                  className={`message ${message.sender}-message`}
                >
                  <div className="message-content">
                    {message.text}
                    {message.sources && message.sources.length > 0 && (
                      <div className="message-sources">
                        Sources: {message.sources.join(', ')}
                      </div>
                    )}
                  </div>
                </div>
              ))
            )}
            {isLoading && (
              <div className="message ai-message">
                <div className="message-content">
                  <div className="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
          
          <div className="chat-input-area">
            <textarea
              ref={textareaRef}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Ask a question about the textbook..."
              disabled={isLoading}
              rows={2}
            />
            <button 
              onClick={handleSend} 
              disabled={!inputValue.trim() || isLoading}
              className="send-button"
            >
              {isLoading ? 'Sending...' : '→'}
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatWidget;