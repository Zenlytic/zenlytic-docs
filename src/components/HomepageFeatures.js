import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'Natural language',
    description: (
      <>
        Zenlytic lets you ask natural language questions of your data.
        Business people can get the answers they need without having to
        figure out every facet of the interface. That's true self-serve.
      </>
    ),
  },
  {
    title: 'Deeper questions',
    description: (
      <>
        Zenlytic helps you answer deeper questions like "Why is my conversion
        rate changing?" or "How are my TikTok customers different?"
        You shouldn't have to spend hours to get the answers you need.
      </>
    ),
  },
  {
    title: 'Interoperable',
    description: (
      <>
        Zenlytic's metrics layer integrates directly with dbt Metricflow. 
        You can reference your semantic models directly in Zenlytic 
        and explore them with Zoë, the AI chatbot, and with full UI functionality.
      </>
    ),
  },
];

function Feature({ Svg, title, description }) {
  return (
    <div style={{ paddingTop: '50px' }} className={clsx('col col--4')}>
      {/* <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div> */}
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
