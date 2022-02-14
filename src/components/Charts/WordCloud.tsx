import { useState } from 'react';
import { Text } from '@visx/text';
import { scaleLog } from '@visx/scale';
import { Wordcloud } from '@visx/wordcloud';
import ParentSize from '@visx/responsive/lib/components/ParentSize';

const totoAfricaLyrics = `I hear the drums echoing tonight
But she hears only whispers of some quiet conversation
She's coming in, 12:30 flight
The moonlit wings reflect the stars that guide me towards salvation
I stopped an old man along the way
Hoping to find some old forgotten words or ancient melodies
He turned to me as if to say, Hurry boy, it's waiting there for you
It's gonna take a lot to drag me away from you
There's nothing that a hundred men or more could ever do
I bless the rains down in Africa
Gonna take some time to do the things we never had ooh, ooh
The wild dogs cry out in the night
As they grow restless, longing for some solitary company
I know that I must do what's right
As sure as Kilimanjaro rises like Olympus above the Serengeti
I seek to cure what's deep inside, frightened of this thing that I've become
It's gonna take a lot to drag me away from you
There's nothing that a hundred men or more could ever do
I bless the rains down in Africa
Gonna take some time to do the things we never had ooh, ooh
Hurry boy, she's waiting there for you
It's gonna take a lot to drag me away from you
There's nothing that a hundred men or more could ever do
I bless the rains down in Africa
I bless the rains down in Africa
I bless the rain
I bless the rains down in Africa I bless the rain
I bless the rains down in Africa
I bless the rains down in Africa ah, gonna take the time
Gonna take some time to do the things we never had ooh, ooh`;


interface ExampleProps {
  width: number;
  height: number;
  showControls?: boolean;
}

export interface WordData {
  text: string;
  value: number;
}

const colors = ['#143059', '#2F6B9A', '#82a6c2'];

function wordFreq(text: string): WordData[] {
  const words: string[] = text.replace(/\./g, '').split(/\s/);
  const freqMap: Record<string, number> = {};

  for (const w of words) {
    if (!freqMap[w]) freqMap[w] = 0;
    freqMap[w] += 1;
  }
  return Object.keys(freqMap).map((word) => ({ text: word, value: freqMap[word] }));
}

function getRotationDegree() {
  const rand = Math.random();
  const degree = rand > 0.5 ? 60 : -60;
  return rand * degree;
}

const words = wordFreq(totoAfricaLyrics);

const fontScale = scaleLog({
  domain: [Math.min(...words.map((w) => w.value)), Math.max(...words.map((w) => w.value))],
  range: [10, 100],
});
const fontSizeSetter = (datum: WordData) => fontScale(datum.value);

const fixedValueGenerator = () => 0.5;

type SpiralType = 'archimedean' | 'rectangular';

export default function WordCloud() {
  const [spiralType] = useState<SpiralType>('archimedean');
  const [withRotation] = useState(false);

  return (
  <div style={{'width':"100%", 'height':"300px"}}>
    <ParentSize>{({width, height}) =>
        <div className="wordcloud">
            <Wordcloud
                words={words}
                width={width}
                height={height}
                fontSize={fontSizeSetter}
                font={'Impact'}
                padding={2}
                spiral={spiralType}
                rotate={withRotation ? getRotationDegree : 0}
                random={fixedValueGenerator}
            >
                {(cloudWords) =>
                    cloudWords.map((w, i) => (
                        <Text
                            key={w.text}
                            fill={colors[i % colors.length]}
                            textAnchor={'middle'}
                            transform={`translate(${w.x}, ${w.y}) rotate(${w.rotate})`}
                            fontSize={w.size}
                            fontFamily={w.font}
                        >
                            {w.text}
                        </Text>
                    ))
                }
            </Wordcloud>
            <style>{`
            .wordcloud {
              display: flex;
              flex-direction: column;
              user-select: none;
            }
            .wordcloud svg {
              margin: 1rem 0;
              cursor: pointer;
            }

            .wordcloud label {
              display: inline-flex;
              align-items: center;
              font-size: 14px;
              margin-right: 8px;
            }
            .wordcloud textarea {
              min-height: 100px;
            }
          `}</style>
        </div>
    }</ParentSize>
  </div>
  );
}