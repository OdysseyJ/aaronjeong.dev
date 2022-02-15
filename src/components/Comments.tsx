import {useEffect} from "react";

type CommentsProps = {
  config: any
}

const Comments: React.FC<CommentsProps> = ({config}) => {
  useEffect(()=>{
    (function() { // DON'T EDIT BELOW THIS LINE
      var d = document, s = d.createElement('script');
      s.src = 'https://aaronjeong.disqus.com/embed.js';
      s.setAttribute('data-timestamp', new Date().toISOString());
      (d.head || d.body).appendChild(s);
    })();
  })

  return (<div id="disqus_thread"></div>)
};

export default Comments;
