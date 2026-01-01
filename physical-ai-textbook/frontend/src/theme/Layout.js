import React from 'react';
import Layout from '@theme-original/Layout';
import ChatWidget from '../components/ChatWidget';

export default function LayoutWithChatWidget(props) {
  return (
    <Layout {...props}>
      {props.children}
      <ChatWidget />
    </Layout>
  );
}