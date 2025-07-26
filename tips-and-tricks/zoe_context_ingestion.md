# How Zoë Ingests Context

Zoë, the AI data analyst, leverages multiple sources of context to understand your data model and provide accurate, relevant responses. This document explains the different ways Zoë learns about your data and how to optimize each source for better results.

## Context Sources

### 1. Customer Context in System Prompt

Custom context added to Zoë's system prompt provides domain-specific knowledge:

- **Industry Context**: Specific business metrics and KPIs relevant to your sector
- **Company Terminology**: Internal terms, abbreviations, and naming conventions
- **Business Rules**: Specific calculation methods or data interpretation guidelines
- **Organizational Structure**: How departments, teams, or business units are organized

**Optimization Tips:**
- Include glossaries of company-specific terms and their definitions
- Document any unique business rules or calculation methodologies
- Explain organizational hierarchies that affect data interpretation
- Provide context about data quality issues or known limitations

### 2. Fine-Tuning Examples

Zoë learns from examples of successfully answered questions to improve her performance:

- **Query Patterns**: Common ways users ask for similar data when she answers successfully
- **Field Usage**: How different measures and dimensions are typically combined

**Optimization Tips:**
- Review Zoë's responses and hit the thumbs up button to reinforce desired behavior using a fine tuning example
- Use the admin panel to remove any undesired or incorrectly "thumbs up" patterns
- Zoë will see how often fields are used in your workspace, and will automatically lean toward re-using the most popular content.

### 3. YAML-Based Views

For traditional Zenlytic setups, Zoë reads directly from your YAML view definitions (see 5 for dbt Metricflow):

- **Field Definitions**: All view, measures, dimensions, and dimension groups. Descriptions pull in automatically from data warehouses like Snowflake, BigQuery and Databricks.
- **Topic Structure**: How views join to each other through topics (including topic descriptions)
- **Access Controls**: What data each user can access (Zoë does not see data a user cannot access, and will block access if requested)
- **Descriptions**: Both user-facing and Zoë-specific descriptions using `description` and `zoe_description` (Zoë will see `description` if `zoe_description` is not defined, and will only see `zoe_description` if both are defined)

**Optimization Tips:**
- Use `zoe_description` fields to provide AI-specific context that differs from user-facing descriptions
- Include business logic explanations in measure and dimension descriptions
- Document edge cases, calculation nuances, or limitations that Zoë should be aware of


### 4. dbt MetricFlow ingestion (Optional)

When using dbt MetricFlow as your semantic layer (instead of Zenlytic's ZenML), Zoë automatically ingests context from your dbt project:

- **Semantic Models**: Automatically mapped to Zenlytic views
- **Measures and Metrics**: Both map to Zenlytic measures.
- **Dimensions**: Converted to Zenlytic dimensions and dimension groups
- **Relationships**: Join logic and entity relationships are preserved and mapped to [topics](../data-modeling/topic.md)
- **Documentation**: Model and field descriptions carry over to help Zoë understand business context

**Optimization Tips:**
- Include rich descriptions in your dbt models and fields
- Use clear, business-friendly naming conventions
- If you need more sophisticated join logic, you can set `use_default_topics` to `false` in the `zenlytic_project.yml` file and define your own [topics](../data-modeling/topic.md) referencing your Metricflow views.


## Best Practices for Context Optimization

### Rich Descriptions
```yaml
# Good: Provides business context
- name: customer_lifetime_value
  field_type: measure
  type: sum
  sql: ${TABLE}.clv
  description: Total revenue expected from a customer over their entire relationship
  zoe_description: Use this for retention analysis and customer segmentation. Calculated using predictive modeling on historical purchase patterns.

# Less helpful: Technical only
- name: customer_lifetime_value
  field_type: measure
  type: sum
  sql: ${TABLE}.clv
```

### Clear Topic Organization
```yaml
# Good: Descriptive topic with Zoë context
type: topic
label: Customer Analytics
base_view: customers
description: Customer data for retention and value analysis
zoe_description: Primary topic for customer health metrics, churn analysis, and segmentation. Includes predictive CLV calculations and behavioral scoring.
```

### Semantic Field Names
Use field names that clearly indicate their business purpose. This is not essential because Zoë has extensive world knowledge, but it is very helpful for both Zoë and your end users:
- `monthly_recurring_revenue` instead of `mrr`
- `customer_acquisition_cost` instead of `cac`
- `days_since_last_purchase` instead of `days_diff`

## Context Hierarchy

Zoë processes context in this priority order:

1. **Customer system prompt context** (company-specific rules and terminology)
2. **Structural relationships** (how data connects through topics and joins, including topic descriptions)
3. **YAML/dbt descriptions** (field and view-level business context)
4. **Fine-tuning examples** (Zoë sees her previous (successful) query patterns)

Understanding this hierarchy helps you place the most critical context in the right locations for maximum impact on Zoë's performance. 