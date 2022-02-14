import ReactPlayer from 'react-player'
import ParentSize from '@visx/responsive/lib/components/ParentSize';

type YoutubePlayerProps = {
    url: string
}

const YoutubePlayer: React.FC<YoutubePlayerProps> = ({ url }) => {
    return (
        <div style={{'width':"100%", 'height':"300px"}}>
            <ParentSize>{({width}) =>
                <ReactPlayer url={url} width={width} />
            }</ParentSize>
        </div>)
}

export default YoutubePlayer
