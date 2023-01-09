// Generated from e:\Semester 4\B-Algorithm\Automata\FunctionDemo\MyGrammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MyGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		ID=18, INT=19, FLOAT=20, BOOL=21, STRING=22, PLUS=23, MINUS=24, MULTIPLY=25, 
		DIVIDE=26, MODULO=27, EQUALS=28, NOT_EQUALS=29, GREATER_THAN=30, LESS_THAN=31, 
		GREATER_THAN_EQUALS=32, LESS_THAN_EQUALS=33, AND=34, OR=35, WS=36;
	public static final int
		RULE_prog = 0, RULE_single_statement = 1, RULE_function_declaration = 2, 
		RULE_parameter_declaration = 3, RULE_block = 4, RULE_statement = 5, RULE_function_call = 6, 
		RULE_print_statement = 7, RULE_return_statement = 8, RULE_assignment = 9, 
		RULE_if_statement = 10, RULE_while_statement = 11, RULE_expression = 12, 
		RULE_type = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "single_statement", "function_declaration", "parameter_declaration", 
			"block", "statement", "function_call", "print_statement", "return_statement", 
			"assignment", "if_statement", "while_statement", "expression", "type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'('", "','", "')'", "'{'", "'}'", "'print'", "'return'", 
			"'='", "'if'", "'else'", "'while'", "'int'", "'float'", "'bool'", "'string'", 
			"'void'", null, null, null, null, null, "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'&&'", "'||'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "ID", "INT", "FLOAT", "BOOL", "STRING", 
			"PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", "EQUALS", "NOT_EQUALS", 
			"GREATER_THAN", "LESS_THAN", "GREATER_THAN_EQUALS", "LESS_THAN_EQUALS", 
			"AND", "OR", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MyGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MyGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public List<Single_statementContext> single_statement() {
			return getRuleContexts(Single_statementContext.class);
		}
		public Single_statementContext single_statement(int i) {
			return getRuleContext(Single_statementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__6) | (1L << T__9) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << ID))) != 0)) {
				{
				{
				setState(28);
				single_statement();
				}
				}
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Single_statementContext extends ParserRuleContext {
		public Function_declarationContext function_declaration() {
			return getRuleContext(Function_declarationContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Print_statementContext print_statement() {
			return getRuleContext(Print_statementContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public While_statementContext while_statement() {
			return getRuleContext(While_statementContext.class,0);
		}
		public Single_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_statement; }
	}

	public final Single_statementContext single_statement() throws RecognitionException {
		Single_statementContext _localctx = new Single_statementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_single_statement);
		try {
			setState(46);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				function_declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(35);
				function_call();
				setState(36);
				match(T__0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(38);
				print_statement();
				setState(39);
				match(T__0);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(41);
				assignment();
				setState(42);
				match(T__0);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(44);
				if_statement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(45);
				while_statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_declarationContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<Parameter_declarationContext> parameter_declaration() {
			return getRuleContexts(Parameter_declarationContext.class);
		}
		public Parameter_declarationContext parameter_declaration(int i) {
			return getRuleContext(Parameter_declarationContext.class,i);
		}
		public Function_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declaration; }
	}

	public final Function_declarationContext function_declaration() throws RecognitionException {
		Function_declarationContext _localctx = new Function_declarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			type();
			setState(49);
			match(ID);
			setState(50);
			match(T__1);
			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16))) != 0)) {
				{
				setState(51);
				parameter_declaration();
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__2) {
					{
					{
					setState(52);
					match(T__2);
					setState(53);
					parameter_declaration();
					}
					}
					setState(58);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(61);
			match(T__3);
			setState(62);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Parameter_declarationContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public Parameter_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_declaration; }
	}

	public final Parameter_declarationContext parameter_declaration() throws RecognitionException {
		Parameter_declarationContext _localctx = new Parameter_declarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_parameter_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			type();
			setState(65);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(T__4);
			setState(71);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__6) | (1L << T__7) | (1L << T__9) | (1L << T__11) | (1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << ID))) != 0)) {
				{
				{
				setState(68);
				statement();
				}
				}
				setState(73);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(74);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Print_statementContext print_statement() {
			return getRuleContext(Print_statementContext.class,0);
		}
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public While_statementContext while_statement() {
			return getRuleContext(While_statementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_statement);
		try {
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(76);
				function_call();
				setState(77);
				match(T__0);
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				print_statement();
				setState(80);
				match(T__0);
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 3);
				{
				setState(82);
				return_statement();
				setState(83);
				match(T__0);
				}
				break;
			case T__12:
			case T__13:
			case T__14:
			case T__15:
			case T__16:
				enterOuterAlt(_localctx, 4);
				{
				setState(85);
				assignment();
				setState(86);
				match(T__0);
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 5);
				{
				setState(88);
				if_statement();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 6);
				{
				setState(89);
				while_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(ID);
			setState(93);
			match(T__1);
			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << ID) | (1L << INT) | (1L << FLOAT) | (1L << BOOL) | (1L << STRING))) != 0)) {
				{
				setState(94);
				expression(0);
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__2) {
					{
					{
					setState(95);
					match(T__2);
					setState(96);
					expression(0);
					}
					}
					setState(101);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(104);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Print_statementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Print_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_statement; }
	}

	public final Print_statementContext print_statement() throws RecognitionException {
		Print_statementContext _localctx = new Print_statementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_print_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(T__6);
			setState(107);
			match(T__1);
			setState(108);
			expression(0);
			setState(109);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_statementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_return_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(T__7);
			setState(112);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			type();
			setState(115);
			match(ID);
			setState(116);
			match(T__8);
			setState(117);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_statementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_if_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(T__9);
			setState(120);
			match(T__1);
			setState(121);
			expression(0);
			setState(122);
			match(T__3);
			setState(123);
			statement();
			setState(126);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(124);
				match(T__10);
				setState(125);
				statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_statementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public While_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_statement; }
	}

	public final While_statementContext while_statement() throws RecognitionException {
		While_statementContext _localctx = new While_statementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(T__11);
			setState(129);
			match(T__1);
			setState(130);
			expression(0);
			setState(131);
			match(T__3);
			setState(132);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MyGrammarParser.ID, 0); }
		public TerminalNode INT() { return getToken(MyGrammarParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(MyGrammarParser.FLOAT, 0); }
		public TerminalNode BOOL() { return getToken(MyGrammarParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(MyGrammarParser.STRING, 0); }
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(MyGrammarParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(MyGrammarParser.MINUS, 0); }
		public TerminalNode MULTIPLY() { return getToken(MyGrammarParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(MyGrammarParser.DIVIDE, 0); }
		public TerminalNode MODULO() { return getToken(MyGrammarParser.MODULO, 0); }
		public TerminalNode EQUALS() { return getToken(MyGrammarParser.EQUALS, 0); }
		public TerminalNode NOT_EQUALS() { return getToken(MyGrammarParser.NOT_EQUALS, 0); }
		public TerminalNode GREATER_THAN() { return getToken(MyGrammarParser.GREATER_THAN, 0); }
		public TerminalNode LESS_THAN() { return getToken(MyGrammarParser.LESS_THAN, 0); }
		public TerminalNode GREATER_THAN_EQUALS() { return getToken(MyGrammarParser.GREATER_THAN_EQUALS, 0); }
		public TerminalNode LESS_THAN_EQUALS() { return getToken(MyGrammarParser.LESS_THAN_EQUALS, 0); }
		public TerminalNode AND() { return getToken(MyGrammarParser.AND, 0); }
		public TerminalNode OR() { return getToken(MyGrammarParser.OR, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(135);
				match(ID);
				}
				break;
			case 2:
				{
				setState(136);
				match(INT);
				}
				break;
			case 3:
				{
				setState(137);
				match(FLOAT);
				}
				break;
			case 4:
				{
				setState(138);
				match(BOOL);
				}
				break;
			case 5:
				{
				setState(139);
				match(STRING);
				}
				break;
			case 6:
				{
				setState(140);
				function_call();
				}
				break;
			case 7:
				{
				setState(141);
				match(T__1);
				setState(142);
				expression(0);
				setState(143);
				match(T__3);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(152);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(147);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(148);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS) | (1L << MINUS) | (1L << MULTIPLY) | (1L << DIVIDE) | (1L << MODULO) | (1L << EQUALS) | (1L << NOT_EQUALS) | (1L << GREATER_THAN) | (1L << LESS_THAN) | (1L << GREATER_THAN_EQUALS) | (1L << LESS_THAN_EQUALS) | (1L << AND) | (1L << OR))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(149);
					expression(2);
					}
					} 
				}
				setState(154);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 12:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3&\u00a0\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\7\2 \n\2\f\2\16\2#\13\2\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\61\n\3\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\7\49\n\4\f\4\16\4<\13\4\5\4>\n\4\3\4\3\4\3\4\3\5\3\5\3\5"+
		"\3\6\3\6\7\6H\n\6\f\6\16\6K\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7]\n\7\3\b\3\b\3\b\3\b\3\b\7\bd\n\b\f\b\16"+
		"\bg\13\b\5\bi\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3"+
		"\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0081\n\f\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16"+
		"\u0094\n\16\3\16\3\16\3\16\7\16\u0099\n\16\f\16\16\16\u009c\13\16\3\17"+
		"\3\17\3\17\2\3\32\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\4\3\2\31%\3"+
		"\2\17\23\2\u00a9\2!\3\2\2\2\4\60\3\2\2\2\6\62\3\2\2\2\bB\3\2\2\2\nE\3"+
		"\2\2\2\f\\\3\2\2\2\16^\3\2\2\2\20l\3\2\2\2\22q\3\2\2\2\24t\3\2\2\2\26"+
		"y\3\2\2\2\30\u0082\3\2\2\2\32\u0093\3\2\2\2\34\u009d\3\2\2\2\36 \5\4\3"+
		"\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\3\3\2\2\2#!\3\2\2"+
		"\2$\61\5\6\4\2%&\5\16\b\2&\'\7\3\2\2\'\61\3\2\2\2()\5\20\t\2)*\7\3\2\2"+
		"*\61\3\2\2\2+,\5\24\13\2,-\7\3\2\2-\61\3\2\2\2.\61\5\26\f\2/\61\5\30\r"+
		"\2\60$\3\2\2\2\60%\3\2\2\2\60(\3\2\2\2\60+\3\2\2\2\60.\3\2\2\2\60/\3\2"+
		"\2\2\61\5\3\2\2\2\62\63\5\34\17\2\63\64\7\24\2\2\64=\7\4\2\2\65:\5\b\5"+
		"\2\66\67\7\5\2\2\679\5\b\5\28\66\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2"+
		";>\3\2\2\2<:\3\2\2\2=\65\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\7\6\2\2@A\5\n\6"+
		"\2A\7\3\2\2\2BC\5\34\17\2CD\7\24\2\2D\t\3\2\2\2EI\7\7\2\2FH\5\f\7\2GF"+
		"\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LM\7\b\2\2M"+
		"\13\3\2\2\2NO\5\16\b\2OP\7\3\2\2P]\3\2\2\2QR\5\20\t\2RS\7\3\2\2S]\3\2"+
		"\2\2TU\5\22\n\2UV\7\3\2\2V]\3\2\2\2WX\5\24\13\2XY\7\3\2\2Y]\3\2\2\2Z]"+
		"\5\26\f\2[]\5\30\r\2\\N\3\2\2\2\\Q\3\2\2\2\\T\3\2\2\2\\W\3\2\2\2\\Z\3"+
		"\2\2\2\\[\3\2\2\2]\r\3\2\2\2^_\7\24\2\2_h\7\4\2\2`e\5\32\16\2ab\7\5\2"+
		"\2bd\5\32\16\2ca\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2fi\3\2\2\2ge\3\2"+
		"\2\2h`\3\2\2\2hi\3\2\2\2ij\3\2\2\2jk\7\6\2\2k\17\3\2\2\2lm\7\t\2\2mn\7"+
		"\4\2\2no\5\32\16\2op\7\6\2\2p\21\3\2\2\2qr\7\n\2\2rs\5\32\16\2s\23\3\2"+
		"\2\2tu\5\34\17\2uv\7\24\2\2vw\7\13\2\2wx\5\32\16\2x\25\3\2\2\2yz\7\f\2"+
		"\2z{\7\4\2\2{|\5\32\16\2|}\7\6\2\2}\u0080\5\f\7\2~\177\7\r\2\2\177\u0081"+
		"\5\f\7\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\27\3\2\2\2\u0082\u0083"+
		"\7\16\2\2\u0083\u0084\7\4\2\2\u0084\u0085\5\32\16\2\u0085\u0086\7\6\2"+
		"\2\u0086\u0087\5\f\7\2\u0087\31\3\2\2\2\u0088\u0089\b\16\1\2\u0089\u0094"+
		"\7\24\2\2\u008a\u0094\7\25\2\2\u008b\u0094\7\26\2\2\u008c\u0094\7\27\2"+
		"\2\u008d\u0094\7\30\2\2\u008e\u0094\5\16\b\2\u008f\u0090\7\4\2\2\u0090"+
		"\u0091\5\32\16\2\u0091\u0092\7\6\2\2\u0092\u0094\3\2\2\2\u0093\u0088\3"+
		"\2\2\2\u0093\u008a\3\2\2\2\u0093\u008b\3\2\2\2\u0093\u008c\3\2\2\2\u0093"+
		"\u008d\3\2\2\2\u0093\u008e\3\2\2\2\u0093\u008f\3\2\2\2\u0094\u009a\3\2"+
		"\2\2\u0095\u0096\f\3\2\2\u0096\u0097\t\2\2\2\u0097\u0099\5\32\16\4\u0098"+
		"\u0095\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2"+
		"\2\2\u009b\33\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009e\t\3\2\2\u009e\35"+
		"\3\2\2\2\r!\60:=I\\eh\u0080\u0093\u009a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}