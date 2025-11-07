# 🚀 Quick Start Guide - ROI Automation System

## 5-Minute Setup

### Prerequisites

```bash
# 1. Install AgentForge
pip install agentforge

# 2. Clone or have access to this repository
cd AgentForge
```

### Step 1: Copy Configuration Files

```bash
# Copy agent prompts to your .agentforge directory
mkdir -p .agentforge/prompts/cog_agents
cp src/agentforge/setup_files/prompts/montreal_revenue_extractor.yaml .agentforge/prompts/
cp src/agentforge/setup_files/prompts/productivity_optimizer.yaml .agentforge/prompts/
cp src/agentforge/setup_files/prompts/graphrag_architect.yaml .agentforge/prompts/
cp src/agentforge/setup_files/prompts/cog_agents/*.yaml .agentforge/prompts/cog_agents/

# Copy cog configuration
mkdir -p .agentforge/cogs
cp src/agentforge/setup_files/cogs/roi_automation_master.yaml .agentforge/cogs/
```

### Step 2: Configure API Keys

Create a `.env` file in your project root:

```bash
# OpenAI (for embeddings and some models)
OPENAI_API_KEY=sk-...

# Anthropic (for Claude models - recommended for complex reasoning)
ANTHROPIC_API_KEY=sk-ant-...

# Google (for Gemini models - fast and cost-effective)
GOOGLE_API_KEY=...

# Optional: For GraphRAG implementation
NEO4J_URI=neo4j+s://...
NEO4J_USER=neo4j
NEO4J_PASSWORD=...
PINECONE_API_KEY=...
```

### Step 3: Test the System

```python
from agentforge.cog import Cog

# Initialize the master cog
roi_cog = Cog('roi_automation_master')

# Test with a simple query
result = roi_cog.run(
    user_input="I want to make $4000 every 2 weeks from AI freelancing"
)

print(result)
```

## Usage Examples

### Example 1: Revenue Analysis

```python
from agentforge.agent import Agent

revenue_agent = Agent('montreal_revenue_extractor')
result = revenue_agent.run(
    current_skills="Prompt engineering, Python, AI automation",
    target_income=4000,
    available_hours=20,
    current_employment="Full-time job",
    additional_context="Based in Montreal, bilingual FR/EN"
)
```

### Example 2: Productivity Optimization

```python
from agentforge.agent import Agent

productivity_agent = Agent('productivity_optimizer')
result = productivity_agent.run(
    work_schedule="15:00-23:00",
    sleep_pattern="01:00-09:00",
    energy_peaks="Morning after waking, late afternoon",
    procrastination_triggers="Complex projects, admin tasks",
    primary_goal="Build freelance business alongside day job",
    deep_work_hours=4
)
```

### Example 3: Knowledge System Design

```python
from agentforge.agent import Agent

knowledge_agent = Agent('graphrag_architect')
result = knowledge_agent.run(
    data_sources=[
        "Gmail (5 years)",
        "Google Drive (200GB)",
        "Notion (500 notes)"
    ],
    monthly_budget=500,
    use_cases=[
        "Research past projects",
        "Find relevant AI techniques",
        "Generate context-aware prompts"
    ]
)
```

## Automation Setup

### Zapier - Administrative Automation

1. Go to [Zapier](https://zapier.com)
2. Create new Zap
3. Import from: `docs/automation_templates/zapier_admin_automation.json`
4. Configure:
   - Gmail connection
   - Google Calendar connection
   - Google Sheets connection
   - Slack/SMS (optional)
5. Test and activate

**Time to setup:** 15 minutes
**Monthly time saved:** 2-3 hours

### Make.com - Crypto Portfolio Tracker

1. Go to [Make.com](https://make.com)
2. Create new scenario
3. Import from: `docs/automation_templates/make_crypto_tracker.json`
4. Configure:
   - Ndax API keys
   - Bitget API keys
   - Google Sheets
   - Notification preferences
5. Test and activate

**Time to setup:** 20 minutes
**Monthly time saved:** 8 hours

## Google Sheets Templates

### Financial Tracking Sheet

Create a Google Sheet with these sheets:

1. **Government Mail Tracking**
   - Columns: Date | Sender | Subject | Has Attachment | Status | Action By | Link | Notes

2. **Crypto Portfolio**
   - Columns: Date | NDAX_BTC | NDAX_ETH | Bitget_BTC | Bitget_ETH | Total_Value_CAD | 24h_Change

3. **AI News Tracking**
   - Columns: Date | Source | Title | Link | Priority | Status | Notes

4. **Task Management**
   - Columns: Week | Task | Deadline | Completed | Hours | ROI Score

5. **Dashboard**
   - Charts for time saved, financial overview, task completion

## Troubleshooting

### Agent not responding

```bash
# Check API keys
python -c "import os; print(os.getenv('ANTHROPIC_API_KEY'))"

# Check configuration
python -c "from agentforge.config import Config; print(Config().data)"
```

### Configuration not found

```bash
# Verify files are in correct location
ls .agentforge/prompts/
ls .agentforge/cogs/

# If missing, copy from setup_files
cp -r src/agentforge/setup_files/prompts/* .agentforge/prompts/
cp -r src/agentforge/setup_files/cogs/* .agentforge/cogs/
```

### Zapier/Make automation not triggering

1. Check trigger configuration (email filters, schedule)
2. Verify API keys and permissions
3. Test each action individually
4. Check error logs in platform

## Next Steps

1. **Week 1**: Set up basic automations (Zapier + Make)
2. **Week 2**: Run revenue extractor and create service packages
3. **Week 3**: Implement productivity protocols
4. **Week 4**: Begin GraphRAG system setup

## ROI Tracking

Track your results weekly:

```markdown
## Week 1 Results

Automations Implemented:
- ✅ Email automation
- ✅ Crypto tracking
- 🔄 AI news digest (in progress)

Time Saved: 5 hours
Cost: $30 (automation tools)
ROI: 16x (5h × $150/h ÷ $30)

Next Week Focus:
- Complete AI news digest
- Launch first client outreach
- Optimize morning deep work routine
```

## Support & Documentation

- **Full Documentation**: [docs/ROI_AUTOMATION_SYSTEM.md](../ROI_AUTOMATION_SYSTEM.md)
- **Example Scripts**: [docs/automation_templates/example_usage.py](./example_usage.py)
- **AgentForge Docs**: https://agentforge.net/
- **GitHub Issues**: https://github.com/DataBassGit/AgentForge/issues

## Success Metrics

Target within 90 days:

- ✅ 30+ hours/month saved through automation
- ✅ $4,000/month freelance income
- ✅ 3 deep work sessions/week
- ✅ <30 seconds to find any past information
- ✅ 10x ROI on automation investment

---

**Ready to maximize your AI automation ROI? Start with Step 1 above! 🚀**
