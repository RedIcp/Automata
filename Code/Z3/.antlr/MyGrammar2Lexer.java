// Generated from /Users/javiercanto/Desktop/Fontys_Automata/Code/Z3/MyGrammar2.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MyGrammar2Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, COMMENT=20, INT_W=21, ID=22, NUMBER=23, WS=24;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "COMMENT", "INT_W", "ID", "NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "'declare-fun'", "')'", "'define-const'", "'assert'", "'distinct'", 
			"'>='", "'<='", "'<'", "'>'", "'='", "'+'", "'-'", "'/'", "'*'", "'and'", 
			"'or'", "'check-sat'", "'get-model'", null, "'Int'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "COMMENT", "INT_W", "ID", 
			"NUMBER", "WS"
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


	public MyGrammar2Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyGrammar2.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32\u00b5\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t"+
		"\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21"+
		"\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25"+
		"\7\25\u0092\n\25\f\25\16\25\u0095\13\25\3\25\3\25\3\25\3\25\3\26\3\26"+
		"\3\26\3\26\3\27\6\27\u00a0\n\27\r\27\16\27\u00a1\3\27\7\27\u00a5\n\27"+
		"\f\27\16\27\u00a8\13\27\3\30\6\30\u00ab\n\30\r\30\16\30\u00ac\3\31\6\31"+
		"\u00b0\n\31\r\31\16\31\u00b1\3\31\3\31\3\u0093\2\32\3\3\5\4\7\5\t\6\13"+
		"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'"+
		"\25)\26+\27-\30/\31\61\32\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2\62;\5\2\13\f"+
		"\17\17\"\"\2\u00b9\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\3\63\3\2\2\2\5\65\3\2\2\2\7A\3\2\2\2\t"+
		"C\3\2\2\2\13P\3\2\2\2\rW\3\2\2\2\17`\3\2\2\2\21c\3\2\2\2\23f\3\2\2\2\25"+
		"h\3\2\2\2\27j\3\2\2\2\31l\3\2\2\2\33n\3\2\2\2\35p\3\2\2\2\37r\3\2\2\2"+
		"!t\3\2\2\2#x\3\2\2\2%{\3\2\2\2\'\u0085\3\2\2\2)\u008f\3\2\2\2+\u009a\3"+
		"\2\2\2-\u009f\3\2\2\2/\u00aa\3\2\2\2\61\u00af\3\2\2\2\63\64\7*\2\2\64"+
		"\4\3\2\2\2\65\66\7f\2\2\66\67\7g\2\2\678\7e\2\289\7n\2\29:\7c\2\2:;\7"+
		"t\2\2;<\7g\2\2<=\7/\2\2=>\7h\2\2>?\7w\2\2?@\7p\2\2@\6\3\2\2\2AB\7+\2\2"+
		"B\b\3\2\2\2CD\7f\2\2DE\7g\2\2EF\7h\2\2FG\7k\2\2GH\7p\2\2HI\7g\2\2IJ\7"+
		"/\2\2JK\7e\2\2KL\7q\2\2LM\7p\2\2MN\7u\2\2NO\7v\2\2O\n\3\2\2\2PQ\7c\2\2"+
		"QR\7u\2\2RS\7u\2\2ST\7g\2\2TU\7t\2\2UV\7v\2\2V\f\3\2\2\2WX\7f\2\2XY\7"+
		"k\2\2YZ\7u\2\2Z[\7v\2\2[\\\7k\2\2\\]\7p\2\2]^\7e\2\2^_\7v\2\2_\16\3\2"+
		"\2\2`a\7@\2\2ab\7?\2\2b\20\3\2\2\2cd\7>\2\2de\7?\2\2e\22\3\2\2\2fg\7>"+
		"\2\2g\24\3\2\2\2hi\7@\2\2i\26\3\2\2\2jk\7?\2\2k\30\3\2\2\2lm\7-\2\2m\32"+
		"\3\2\2\2no\7/\2\2o\34\3\2\2\2pq\7\61\2\2q\36\3\2\2\2rs\7,\2\2s \3\2\2"+
		"\2tu\7c\2\2uv\7p\2\2vw\7f\2\2w\"\3\2\2\2xy\7q\2\2yz\7t\2\2z$\3\2\2\2{"+
		"|\7e\2\2|}\7j\2\2}~\7g\2\2~\177\7e\2\2\177\u0080\7m\2\2\u0080\u0081\7"+
		"/\2\2\u0081\u0082\7u\2\2\u0082\u0083\7c\2\2\u0083\u0084\7v\2\2\u0084&"+
		"\3\2\2\2\u0085\u0086\7i\2\2\u0086\u0087\7g\2\2\u0087\u0088\7v\2\2\u0088"+
		"\u0089\7/\2\2\u0089\u008a\7o\2\2\u008a\u008b\7q\2\2\u008b\u008c\7f\2\2"+
		"\u008c\u008d\7g\2\2\u008d\u008e\7n\2\2\u008e(\3\2\2\2\u008f\u0093\7=\2"+
		"\2\u0090\u0092\13\2\2\2\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093"+
		"\u0094\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093\3\2"+
		"\2\2\u0096\u0097\7\f\2\2\u0097\u0098\3\2\2\2\u0098\u0099\b\25\2\2\u0099"+
		"*\3\2\2\2\u009a\u009b\7K\2\2\u009b\u009c\7p\2\2\u009c\u009d\7v\2\2\u009d"+
		",\3\2\2\2\u009e\u00a0\t\2\2\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2"+
		"\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a6\3\2\2\2\u00a3\u00a5"+
		"\t\3\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6"+
		"\u00a7\3\2\2\2\u00a7.\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ab\t\4\2\2"+
		"\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad"+
		"\3\2\2\2\u00ad\60\3\2\2\2\u00ae\u00b0\t\5\2\2\u00af\u00ae\3\2\2\2\u00b0"+
		"\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2"+
		"\2\2\u00b3\u00b4\b\31\2\2\u00b4\62\3\2\2\2\b\2\u0093\u00a1\u00a6\u00ac"+
		"\u00b1\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}