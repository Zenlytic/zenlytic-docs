import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './HomepageFeatures.module.css';

const DocCategories = [
  {
    title: 'Tips and Tricks',
    description: 'Essential tips and tricks for getting the most out of Zenlytic and Zoë',
    docId: 'category/tips-and-tricks',
  },
  {
    title: 'Using Zenlytic',
    description: 'Learn how to use Zenlytic\'s powerful interface features and capabilities',
    docId: 'category/using-zenlytic',
  },
  {
    title: 'Embedding',
    description: 'Discover how to embed Zenlytic\'s analytics capabilities into your applications',
    docId: 'category/embedding',
  },
  {
    title: 'Data Modeling',
    description: 'Learn how to model your data effectively in Zenlytic for optimal analytics performance',
    docId: 'category/data-modeling',
  },
  {
    title: 'Workflows',
    description: 'Explore Zenlytic\'s workflow capabilities for automating and streamlining your analytics processes',
    docId: 'category/workflows',
  },
  {
    title: 'Development Environment',
    description: 'Set up and configure your development environment for working with Zenlytic',
    docId: 'category/development-environment',
  },
  {
    title: 'Connecting with Python',
    description: 'Learn how to integrate Zenlytic with Python for advanced analytics capabilities',
    docId: 'category/connecting-with-python',
  },
  {
    title: 'About',
    description: 'Learn more about Zenlytic, our mission, and how we can help you with your analytics needs',
    docId: 'category/about',
  },
];

function DocCard({ title, description, docId }) {
  return (
    <div className={clsx('col col--3', styles.card)}>
      <Link to={`/docs/${docId}`} className={styles.cardLink}>
        <div className={styles.cardContent}>
          <h3>{title}</h3>
          <p>{description}</p>
        </div>
      </Link>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {DocCategories.map((props, idx) => (
            <DocCard key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
