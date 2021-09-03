import React from 'react';
import withToasts from 'src/messageToasts/enhancers/withToasts';


interface AIPageProps {
  addSuccessToast: (msg: string) => void;
  user: {
    userId: string | number;
  };
}


function AiPage(props: AIPageProps) {
  return(
    <h1>Hello, AI!</h1>
  )
}

export default withToasts(AiPage);